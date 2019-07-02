import { browser, by, element } from 'protractor';
import { CommonPO } from './common.po';

export class AppPage extends CommonPO {
  navigateTo() {
    return browser.get(browser.baseUrl) as Promise<any>;
  }
}
