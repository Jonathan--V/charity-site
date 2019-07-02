import { EventsPage } from './page-objects/events-page.po';
import { CommonTest } from './common';

let specificTests = (getPage: () => EventsPage) => {
  return () => {
    it('should list no events', () => {
      expect(getPage().getEvents()).toEqual({});
    })
    it('should display a log in button', () => {
      expect(getPage().getLoginButtonText()).toEqual('login');
    });
  }
}

CommonTest.commonTest('Events Page', EventsPage, specificTests)
