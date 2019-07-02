import { browser, by, element } from 'protractor';
import { CommonPO } from './common.po';

export class EventDetailPage extends CommonPO {

  constructor(id: number = 1) {
    super()
    this.id = id;
  }

  navigateTo() {
    return browser.get(`${browser.baseUrl}events/${this.id}`) as Promise<any>;
  }

}