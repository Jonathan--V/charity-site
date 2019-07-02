import { browser, by, element, protractor } from 'protractor';
import { CommonPO } from './common.po';

export class EventsPage extends CommonPO {
  navigateTo() {
    return browser.get(`${browser.baseUrl}events`) as Promise<any>;
  }
  getEvents(): object {
    console.log("in getEvents()")
    let events = {}
    return element.all(by.id("events_repeater")).all(by.className("event_link")).then(function (elements) {
      let promises = []
      for (let elem of elements) {
        let url
        let href_promise = elem.getAttribute("href")
        promises.push(href_promise)
        href_promise.then(function (href) {
          console.log(href)
          url = href
        })
        let text_promise = elem.getText()
        promises.push(text_promise)
        text_promise.then(function (text) {
          console.log(text)
          events[url] = text;
        })
      }
      return protractor.promise.all(promises).then(_ => {
        return events;
      })
    });
    
  }
}