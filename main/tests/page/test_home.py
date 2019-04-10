from main.tests.page.common import CommonTest


class TestHome(CommonTest):

    def test_home(self):
        for driver in self.drivers:
            print(f"Testing home page using driver {driver.name}")
            driver.get(self.live_server_url)
            self.check_equal("Charitee", driver.title)
            self.check_equal("Welcome to to the home page!", driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Submit'])[1]/following::p[1]").text)
            self.check_image('-606C9F26', "home_image", driver)

