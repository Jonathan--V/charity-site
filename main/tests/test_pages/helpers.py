class Helpers:
    @staticmethod
    def log_into_admin_site(driver, live_server_url):
        driver.get(f"{live_server_url}/admin")
        if driver.find_elements_by_id("id_password"):
            # we are not yet logged in
            username = "test_admin"
            password = "test_password1"
            driver.find_element_by_id("id_username").send_keys(username)
            driver.find_element_by_id("id_password").send_keys(password)
            driver.find_element_by_xpath("//input[@type='submit']").click()

    @staticmethod
    def convert_date_to_locale_format(driver, date):
        return driver.execute_script(
            f'return (new Date('
            f'{date.year}, '
            f'{date.month - 1}, '  # the month in Javascript is 0-based.
            f'{date.day}))'
            f'.toLocaleDateString()'
        )
