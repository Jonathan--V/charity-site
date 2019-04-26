import contextlib
import os
import subprocess
from datetime import datetime, timedelta
from time import sleep
from unittest import TestCase

import psutil
import requests
from selenium.webdriver import firefox, chrome
from selenium.webdriver.support.wait import WebDriverWait


class CommonTest(TestCase):
    TEST_DB_NAME = 'test_db.sqlite3'

    def setUp(self):
        print()
        super().setUp()
        self.port = '8001'
        self.live_server_url = f"http://localhost:{self.port}"
        self.verification_errors = []
        self.url_root = self.live_server_url
        self._database_setup()
        self._launch_django_server()
        self._selenium_driver_setup()
        self._wait_until_server_available()

    def _database_setup(self):
        """
        Prepares a new sqlite database using the schema from the main database but none of the data.
        Then, inserts test data into it via Django.
        """

        with contextlib.suppress(FileNotFoundError):
            TIMEOUT_SECONDS = 60
            cutoff_time = datetime.now() + timedelta(seconds=TIMEOUT_SECONDS)
            db_deleted = False
            while not db_deleted and datetime.now() < cutoff_time:
                try:
                    os.remove(self.TEST_DB_NAME)
                    db_deleted = True
                except PermissionError:
                    # DB file lock is probably still held by last django server instance.
                    # Let's give it a moment to release it.
                    pass

            if not db_deleted:
                raise TimeoutError(f"Could not delete {self.TEST_DB_NAME}")

        # Just doing:
        # `subprocess.call(f'sqlite3 db.sqlite3 .schema | sqlite3 {self.TEST_DB_NAME}', shell=True)`
        # would be nicer, but unfortunately sqlite creates a default table (sqlite_sequence) that we need to
        # remove from the schema before passing it back in again
        schema_byte_string = subprocess.check_output('sqlite3 db.sqlite3 .schema', shell=True)
        schema_string = str(schema_byte_string, 'utf-8')
        schema_one_line = schema_string.replace('\r','').replace('\n','')
        schema_without_sqlite_sequence = schema_one_line.replace('CREATE TABLE sqlite_sequence(name,seq);','')
        subprocess.call(f'echo {schema_without_sqlite_sequence} | sqlite3 {self.TEST_DB_NAME}', shell=True)

        # populate new database as is needed for testing
        with open('logs/test_setup_log.txt', 'a') as log:
            subprocess.call(
                ['py', 'manage.py', 'test_setup', '--settings=charity_configuration.test_settings'],
                stdout=log,
            )

    def _launch_django_server(self):
        with open('logs/test_server_log.txt', 'a') as log:
            log.write("Launching new Django server")
            log.flush()
            self.server_process = subprocess.Popen(
                ['py', 'manage.py', 'runserver', self.port, '--settings=charity_configuration.test_settings'],
                stdout=log,
                stderr=log,
            )

    def _selenium_driver_setup(self):
        browser_string = os.getenv("charity_site_test_browser", "firefox")
        self.browser = browser_string.casefold()
        self.driver = None
        if "firefox".casefold() in self.browser:
            self.firefox_driver = firefox.webdriver.WebDriver(executable_path=r"geckodriver.exe")
            self.firefox_driver.implicitly_wait(10)
            self.driver = self.firefox_driver
        if "chrome".casefold() in self.browser:
            self.chromedriver = chrome.webdriver.WebDriver(executable_path=r"chromedriver.exe")
            self.chromedriver.implicitly_wait(10)
            assert self.driver is None, \
                "The charity_site_test_browser environment variable must only refer to one browser." \
                f" Currently, it is interpreted as {browser_string}." \
                " To test in multiple browsers, set the charity_site_test_browsers variable" \
                " and use the run_tests script."
            self.driver = self.chromedriver
        assert self.driver is not None, \
            "The charity_site_test_browser environment variable must refer to a browser." \
            f" Currently, it is interpreted as {browser_string}."

    def _wait_until_server_available(self):
        TIMEOUT_SECONDS = 60
        cutoff_time = datetime.now() + timedelta(seconds=TIMEOUT_SECONDS)
        connection_achieved = False
        while not connection_achieved and datetime.now() < cutoff_time:
            sleep(1)
            try:
                request = requests.head(f"{self.live_server_url}/en-gb/", headers={'Connection':'close'})
                if request.status_code == 200:
                    connection_achieved = True
            except requests.ConnectionError:
                print("failed to connect")

        if not connection_achieved:
            raise TimeoutError("Could not connect to Django test server.")

    def tearDown(self):
        self.driver.quit()
        # We cannot simply use `self.server_process.terminate()` as this will not actually kill the underlying server
        process = psutil.Process(self.server_process.pid)
        for child_process in process.children(recursive=True):
            child_process.kill()
        process.kill()
        self.server_process.wait()
        self.assertEqual([], self.verification_errors)
        super().tearDown()

    def check_equal(self, expected_value, actual_value):
        try: self.assertEqual(expected_value, actual_value)
        except AssertionError as e: self.verification_errors.append(str(e))

    def check_image(self, expected_hash, image_id):
        image_hash = self.driver.execute_script(self.JS_GET_IMAGE_HASH, self.driver.find_element_by_id(image_id))
        self.check_equal(expected_hash, image_hash)

    def wait_for_page_load(self, old_url):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url != old_url)

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


