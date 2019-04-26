from main.tests.test_pages.common import CommonTest
from main.tests.test_pages.helpers import Helpers


class TestContact(CommonTest):

    def test_contact(self):
        driver = self.driver
        print(f"Testing contact page")
        driver.get(f"{self.live_server_url}/contact/")
        self.check_equal("Charitee | Contact us!", driver.title)
        main_text = \
            """Contact us by:
            Phone: 01234 567 890
            Mail:
            1 Primrose St,
            London
            EC2A 2JN
            Or fill in the online form below:"""

        # ignore whitespace issues
        self.check_equal(' '.join(main_text.split()), ' '.join(driver.find_element_by_id("main_text").text.split()))

        subject = f"Can I help? ({driver.name})"
        email_address = "helper@example.com"
        name = "Helen"
        description = "I would like to help. Please let me know how I can volunteer."

        self.check_equal("Subject:", driver.find_element_by_id("form_table_row_1_label").text)
        self.check_equal("Email address:", driver.find_element_by_id("form_table_row_2_label").text)
        self.check_equal("Name:", driver.find_element_by_id("form_table_row_3_label").text)
        self.check_equal("Description:", driver.find_element_by_id("form_table_row_4_label").text)

        driver.find_element_by_id("id_subject").send_keys(subject)
        driver.find_element_by_id("id_email_address").send_keys(email_address)
        driver.find_element_by_id("id_name").send_keys(name)
        driver.find_element_by_id("id_description").send_keys(description)
        old_url = driver.current_url
        driver.find_element_by_id("form_submit").click()

        self.wait_for_page_load(old_url)
        self.check_equal(f"{self.live_server_url}/en-gb/contact_request_received/", driver.current_url)
        self.check_equal("Charitee | Contact request received!", driver.title)
        self.check_equal("Thank you for contacting us!", driver.find_element_by_id("main_text").text)
        self.check_image('772688B0', "main_image")

        # verify data is viewable in admin site

        Helpers.log_into_admin_site(driver, self.live_server_url)
        driver.find_element_by_xpath("//*[contains(text(), 'Contact requests')]").click()
        driver.find_element_by_xpath(f"//*[contains(text(), '{subject}')]").click()
        self.check_equal(subject, driver.find_element_by_id("id_subject").get_attribute("value"))
        self.check_equal(email_address, driver.find_element_by_id("id_email_address").get_attribute("value"))
        self.check_equal(name, driver.find_element_by_id("id_name").get_attribute("value"))
        self.check_equal(description, driver.find_element_by_id("id_description").get_attribute("value"))




