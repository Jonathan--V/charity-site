import { EventsPage } from './page-objects/events-page.po';
import { browser, logging } from 'protractor';
import { Common } from './common';

describe('Events Page', () => {
  let eventsPage: EventsPage;

  beforeEach(() => {
    eventsPage = new EventsPage();
    eventsPage.navigateTo();
  });

  afterEach(async () => {
    // Protractor's system for accessing logs is currently broken in Firefox.
    if (browser.name === "chrome") {
      console.log("Reached")
      const logs = await browser.manage().logs().get(logging.Type.BROWSER);
      expect(logs).not.toContain(jasmine.objectContaining({
        level: logging.Level.SEVERE,
      } as logging.Entry));
    }

  });
});
