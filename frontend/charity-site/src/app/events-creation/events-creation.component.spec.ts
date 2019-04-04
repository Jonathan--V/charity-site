import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EventsCreationComponent } from './events-creation.component';

describe('EventsCreationComponent', () => {
  let component: EventsCreationComponent;
  let fixture: ComponentFixture<EventsCreationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EventsCreationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EventsCreationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
