import { AppPage } from './page-objects/app.po';
import { browser, logging } from 'protractor';

describe('workspace-project App', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
  });

  // TODO Find a way of running these on each page, not just the homepage

  it('should be titled correctly', () => {
    page.navigateTo();
    expect(page.getTitleText()).toEqual('EVENTS');
  });

  it('should display the navbar', () => {
    expect(page.getEventsListButtonText()).toEqual('Events list');
    expect(page.getCreateEventButtonText()).toEqual('Create event');
    expect(page.getBackToMainSiteButtonText()).toEqual('Back to main site');
  });

  it('should display a log in button', () => {
    expect(page.getLoginButtonText()).toEqual('login');
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
