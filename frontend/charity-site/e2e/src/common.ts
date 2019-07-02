import { browser, logging } from 'protractor';
import { CommonPO } from './page-objects/common.po';

export class CommonTest {
  static commonRunOnce = false
  static commonTest<PageObject extends CommonPO>(name: string, Page: new () => PageObject, specificTests: (pageGetter: () => PageObject) => (() => void) = null): void
  {
    describe(name, () => {
      let page: PageObject;
      if (browser.params['fast']) {
        beforeAll(() => {
          page = new Page();
          page.navigateTo();
        });
      }
      else {
        beforeEach(() => {
          page = new Page();
          page.navigateTo();
        });
      }
      function getPage(){
        return page
      };

      if (!browser.params['fast'] || !this.commonRunOnce) {
        this.commonRunOnce = true
        describe('Common', () => {
          it('should be titled correctly', () => {
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
        });
      }
      
      if (specificTests != null) {
        describe('Page-specific', specificTests(getPage));
      }

      afterEach(async () => {
        // Protractor's system for accessing logs is currently broken in Firefox.
        if (browser.name === "chrome") {
          const logs = await browser.manage().logs().get(logging.Type.BROWSER);
          expect(logs).not.toContain(jasmine.objectContaining({
            level: logging.Level.SEVERE,
          } as logging.Entry));
        }

      });
      
    })
  }
}