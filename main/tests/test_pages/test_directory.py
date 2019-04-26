from types import SimpleNamespace

from main.tests.test_pages.common import CommonTest


class TestDirectory(CommonTest):

    def test_directory(self):
        print(f"Testing directory page")
        driver = self.driver
        driver.get(f"{self.live_server_url}/directory")
        self.check_equal("Charitee | Directory", driver.title)
        self.check_equal("Area of Responsibility", driver.find_element_by_id("area_of_responsibility_header").text)
        self.check_equal("Title", driver.find_element_by_id("title_header").text)
        self.check_equal("First name", driver.find_element_by_id("first_name_header").text)
        self.check_equal("Last name", driver.find_element_by_id("last_name_header").text)
        self.check_equal("Email address", driver.find_element_by_id("email_address_header").text)
        self.contact = SimpleNamespace(
            area_of_responsibility="Head of Communications",
            title="Ms",
            first_name="Chats",
            last_name="Daily",
            email_address="Chats.Daily@example.com",
            publicly_viewable=True,
        )
        self.check_equal(self.contact.area_of_responsibility,
                         driver.find_element_by_id("area_of_responsibility_row_1").text)
        self.check_equal(self.contact.title, driver.find_element_by_id("title_row_1").text)
        self.check_equal(self.contact.first_name, driver.find_element_by_id("first_name_row_1").text)
        self.check_equal(self.contact.last_name, driver.find_element_by_id("last_name_row_1").text)
        self.check_equal(self.contact.email_address, driver.find_element_by_id("email_address_row_1").text)
