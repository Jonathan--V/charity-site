import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import firefox, chrome


class CommonTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        browser_string = os.getenv("charity_site_test_browsers", "firefox,chrome")
        self.browsers = [ browser.casefold() for browser in browser_string.split(',') ]
        self.drivers = []
        if "firefox".casefold() in self.browsers:
            self.firefox_driver = firefox.webdriver.WebDriver(executable_path = r"geckodriver.exe")
            self.firefox_driver.implicitly_wait(10)
            self.drivers.append(self.firefox_driver)
        if "chrome".casefold() in self.browsers:
            self.chromedriver = chrome.webdriver.WebDriver()
            self.chromedriver.implicitly_wait(10)
            self.drivers.append(self.chromedriver)
        self.verificationErrors = []
        self.url_root = self.live_server_url

    def tearDown(self):
        # With the chromedriver,  self.driver.quit() causes a ConnectionResetError.
        # Calling it only for the geckodriver seems to have no adverse effects
        # as the chromedriver process closes down anyway.
        if "firefox".casefold() in self.browsers:
            self.firefox_driver.quit()
        super().tearDown()
        self.assertEqual([], self.verificationErrors)

    def check_equal(self, expected_value, actual_value):
        try: self.assertEqual(expected_value, actual_value)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def check_image(self, expected_hash, image_id, driver):
        image_hash = driver.execute_script(self.JS_GET_IMAGE_HASH, driver.find_element_by_id(image_id))
        self.check_equal(expected_hash, image_hash)

    # from https://stackoverflow.com/questions/36930362/is-there-a-way-in-selenium-through-which-we-can-verify-that-the-image-displayed/36932492
    JS_GET_IMAGE_HASH = """
        var hash = 0, ele = arguments[0], xhr = new XMLHttpRequest();
        var src = ele.src || window.getComputedStyle(ele).backgroundImage;
        xhr.open('GET', src.match(/https?:[^\"')]+/)[0], false);
        xhr.send();
        for (var i = 0, buffer = xhr.response; i < buffer.length; i++)
          hash = (((hash << 5) - hash) + buffer.charCodeAt(i)) | 0;
        return hash.toString(16).toUpperCase();
        """


