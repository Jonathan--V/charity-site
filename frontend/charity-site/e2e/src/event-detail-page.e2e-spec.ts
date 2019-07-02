
import { CommonTest } from './common';
import { EventDetailPage } from './page-objects/event-detail-page.po';

let specificTests = (getPage: () => EventDetailPage) => {
  return () => {

  }
}

CommonTest.commonTest('Event Detail Page', EventDetailPage, specificTests)
