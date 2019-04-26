from main.tests.test_pages.common import CommonTest


class TestHome(CommonTest):

    def test_home(self):
        print(f"Testing home page")
        driver = self.driver
        driver.get(self.live_server_url)
        self.check_equal("Charitee", driver.title)
        self.check_equal("Welcome to to the home page!", driver.find_element_by_id("main_text").text)
        self.check_image('-606C9F26', "main_image")
