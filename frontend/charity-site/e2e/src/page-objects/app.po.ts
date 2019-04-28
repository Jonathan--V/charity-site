import { browser, by, element } from 'protractor';
import { Common } from './common.po';

export class AppPage extends Common {
  navigateTo() {
    return browser.get(browser.baseUrl) as Promise<any>;
  }
}
