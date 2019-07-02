import { browser, by, element } from 'protractor';
import { CommonPO } from './common.po';
import { EventInformation } from '../../../src/app/event-information';

export class EventCreationPage extends CommonPO {
  navigateTo() {
    return browser.get(`${browser.baseUrl}events/create`) as Promise<any>;
  }

  createEvent(eventInformation: EventInformation) {
    element(by.id("event_name")).sendKeys(eventInformation.name);
    element(by.id("event_location")).sendKeys(eventInformation.location);
    element(by.id("event_date")).sendKeys(eventInformation.date.toLocaleDateString());
    element(by.id("event_description")).sendKeys(eventInformation.description);
    element(by.id("create_event_button")).click();
  }

}