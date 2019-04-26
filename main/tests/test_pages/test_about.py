from main.tests.test_pages.common import CommonTest


class TestAbout(CommonTest):

    def test_about(self):
        print(f"Testing about page")
        driver = self.driver
        driver.get(f"{self.live_server_url}/about")
        self.check_equal("Charitee | About us!", driver.title)
        self.check_equal("About us!", driver.find_element_by_id("main_text").text)
        self.check_image('-5F738C0B', "main_image")

