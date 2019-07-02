import { browser, by, element } from 'protractor';

export abstract class CommonPO {

  static stamp = 0

  id: number

  constructor(){
    this.id = CommonPO.stamp++;
  }

  abstract navigateTo();

  getTitleText() {
    return element(by.css('app-root h1')).getText() as Promise<string>;
  }

  getEventsListButtonText() {
    return element(by.id('events_list_link')).getText() as Promise<string>;
  }
  
  getCreateEventButtonText() {
    return element(by.id('create_event_link')).getText() as Promise<string>;
  }

  getBackToMainSiteButtonText() {
    return element(by.id('back_to_main_site_link')).getText() as Promise<string>;
  }

  getLoginButtonText() {
    return element(by.id('login_button')).getText() as Promise<string>;
  }

  logout() {
    let logout_button = element(by.id('logout_button'))
    return logout_button.isDisplayed().then(displayed => {
      if (displayed) {
        return logout_button.click().then(_ => {
          return true;
        })
      }
      else {
        return false
      }
    })
  }

}