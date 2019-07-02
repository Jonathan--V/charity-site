
import { EventInformation } from '../../src/app/event-information';
import { CommonTest } from './common';
import { EventCreationPage } from './page-objects/event-creation-page.po';
import { LoginPage, USERNAME } from './page-objects/login-page.po';


let testEventInformation1 = new EventInformation(USERNAME, new Date("2020-01-01"), "Description: 10: 00 start!", "City Hall, Example Town", "Example Event")

let testEventInformation2 = new EventInformation(USERNAME, new Date("2020-02-01"), "All Day.", "The Clock Tower, Example Town", "Another Example Event")

let specificTests = (getPage: () => EventCreationPage) => {
  return () => {
    it('can create events', () => {
      new LoginPage().login()
      getPage().createEvent(testEventInformation1)
      getPage().logout()
    })
  }
}

CommonTest.commonTest('Event Creation Page', EventCreationPage, specificTests)
