from main.tests.test_pages.common import CommonTest


class TestNavbar(CommonTest):

    def test_navbar(self):
        print(f"Testing navbar")
        driver = self.driver
        driver.get(self.live_server_url)
        driver.find_element_by_link_text("Home").click()
        self.check_equal(f"{self.url_root}/en-gb/", driver.current_url)
        driver.find_element_by_link_text("About").click()
        self.check_equal(f"{self.url_root}/en-gb/about/", driver.current_url)
        driver.find_element_by_link_text("Request Help").click()
        self.check_equal(f"{self.url_root}/en-gb/request_help/", driver.current_url)
        driver.find_element_by_link_text("Directory").click()
        self.check_equal(f"{self.url_root}/en-gb/directory/", driver.current_url)
        driver.find_element_by_link_text("Contact").click()
        self.check_equal(f"{self.url_root}/en-gb/contact/", driver.current_url)

        driver.find_element_by_id("switch_to_fr").click()
        self.check_equal(f"{self.url_root}/fr/contact/", driver.current_url)
        driver.find_element_by_link_text("Annuaire").click()
        self.check_equal(f"{self.url_root}/fr/annuaire/", driver.current_url)
        driver.find_element_by_link_text("Demander de l'aide").click()
        self.check_equal(f"{self.url_root}/fr/demande_daide/", driver.current_url)
        driver.find_element_by_link_text(u"À propos").click()
        self.check_equal(f"{self.url_root}/fr/a_propos/", driver.current_url)
        driver.find_element_by_link_text("Accueil").click()
        self.check_equal(f"{self.url_root}/fr/", driver.current_url)
        driver.find_element_by_id("switch_to_en-gb").click()
        self.check_equal(f"{self.url_root}/en-gb/", driver.current_url)
