import { browser, by, element } from 'protractor';
import { CommonPO } from './common.po';

export let USERNAME = "test_admin"

export class LoginPage extends CommonPO {

  navigateTo() {
    return browser.get(`${browser.baseUrl}login`) as Promise<any>;
  }

  login() {
    element(by.id("username")).sendKeys(USERNAME)
    element(by.id("password")).sendKeys("test_password1")
    element(by.id("log_in_button")).click()
  }

  getLoggedInText() {
    return element(by.id("logged_in_text")).getText()
  }
  
}