import { TestBed } from '@angular/core/testing';

import { DrfCommunicationService } from './drf-communication.service';

describe('DrfCommunicationService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DrfCommunicationService = TestBed.get(DrfCommunicationService);
    expect(service).toBeTruthy();
  });
});
