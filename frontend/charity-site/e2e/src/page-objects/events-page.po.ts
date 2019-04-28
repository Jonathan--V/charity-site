import { browser, by, element } from 'protractor';
import { Common } from '../common';

export class EventsPage extends Common {
  navigateTo() {
    return browser.get(browser.baseUrl) as Promise<any>;
  }

  getTitleText() {
    return element(by.css('app-root h1')).getText() as Promise<string>;
  }
}