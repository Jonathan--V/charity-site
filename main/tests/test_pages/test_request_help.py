import datetime

from main.tests.test_pages.common import CommonTest
from main.tests.test_pages.helpers import Helpers


class TestRequestHelp(CommonTest):

    def test_request_help(self):
        print(f"Testing request help page")
        driver = self.driver

        title = "Lieutenant"
        first_name = "Frank"
        last_name = f"Drebin ({driver.name})"
        email_address = "Frank.Drebin@policesquad.example.com"
        date_of_birth = "1933-04-21"
        date_of_birth_as_date = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')

        brief_summary_of_difficulty = f"Difficulty Parking ({driver.name})"
        how_can_we_help_you = "I invariably crash into parked cars. Teach me how I can stop doing this."

        driver.get(f"{self.live_server_url}/request_help")
        self.check_equal("Charitee | Ask for Help!", driver.title)
        self.check_equal("Title:", driver.find_element_by_id("form_table_row_1_label").text)
        self.check_equal("First name:", driver.find_element_by_id("form_table_row_2_label").text)
        self.check_equal("Last name:", driver.find_element_by_id("form_table_row_3_label").text)
        self.check_equal("Email address:", driver.find_element_by_id("form_table_row_4_label").text)
        self.check_equal("Date of birth:", driver.find_element_by_id("form_table_row_5_label").text)

        driver.find_element_by_id("id_title").send_keys(title)
        driver.find_element_by_id("id_first_name").send_keys(first_name)
        driver.find_element_by_id("id_last_name").send_keys(last_name)
        driver.find_element_by_id("id_email_address").send_keys(email_address)

        # Unfortunately, entering information into date inputs needs to be special-cased by browser:
        if driver.name == "chrome":
            locale_format_date_of_birth = Helpers.convert_date_to_locale_format(driver, date_of_birth_as_date)
            driver.find_element_by_id("id_date_of_birth").send_keys(locale_format_date_of_birth)
        else:
            driver.find_element_by_id("id_date_of_birth").send_keys(date_of_birth)
        old_url = driver.current_url
        driver.find_element_by_id("form_submit").click()

        # page 2
        self.wait_for_page_load(old_url)
        self.check_equal(f"{self.live_server_url}/en-gb/request_help_page_2/", driver.current_url)
        self.check_equal("Charitee | Ask for Help!", driver.title)
        self.check_equal("Brief summary of difficulty:", driver.find_element_by_id("form_table_row_1_label").text)
        self.check_equal("How can we help you?", driver.find_element_by_id("form_table_row_2_label").text)

        driver.find_element_by_id("id_brief_summary_of_difficulty").send_keys(brief_summary_of_difficulty)
        driver.find_element_by_id("id_how_can_we_help_you").send_keys(how_can_we_help_you)
        old_url = driver.current_url
        driver.find_element_by_id("form_submit").click()

        # request received page
        self.wait_for_page_load(old_url)

        self.check_equal(f"{self.live_server_url}/en-gb/request_help_received/", driver.current_url)
        self.check_equal("Charitee | Help request received!", driver.title)
        self.check_equal("Thank you for submitting your request for help!", driver.find_element_by_id("main_text").text)
        self.check_image('772688B0', "main_image")

        # verify data is viewable in admin site

        Helpers.log_into_admin_site(driver, self.live_server_url)
        driver.find_element_by_xpath("//*[contains(text(), 'Persons')]").click()
        driver.find_element_by_xpath(f"//*[contains(text(), '{first_name} {last_name}')]").click()
        self.check_equal(title, driver.find_element_by_id("id_title").get_attribute("value"))
        self.check_equal(first_name, driver.find_element_by_id("id_first_name").get_attribute("value"))
        self.check_equal(last_name, driver.find_element_by_id("id_last_name").get_attribute("value"))
        self.check_equal(email_address, driver.find_element_by_id("id_email_address").get_attribute("value"))
        expected_date_in_locale_format = Helpers.convert_date_to_locale_format(driver, date_of_birth_as_date)
        actual_date_in_locale_format = driver.find_element_by_id("id_date_of_birth").get_attribute("value")
        self.check_equal(expected_date_in_locale_format, actual_date_in_locale_format)
        driver.get(f"{self.live_server_url}/admin")
        driver.find_element_by_xpath("//*[contains(text(), 'Help requests')]").click()
        driver.find_element_by_xpath(f"//*[contains(text(), '{brief_summary_of_difficulty}')]").click()
        self.check_equal(brief_summary_of_difficulty,
                         driver.find_element_by_id("id_brief_summary_of_difficulty").get_attribute("value"))
        self.check_equal(how_can_we_help_you, driver.find_element_by_id("id_how_can_we_help_you").text)
