import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { EventInformation } from "src/app/event-information";


@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {
  

  eventsUrl: string = "http://localhost:8000/en-gb/events/api/events/"
  events: EventInformation[] = []

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getEvents();
  }

  getEventsObservable(): Observable<EventInformation[][]> {
    return this.http.get<EventInformation[][]>(this.eventsUrl)
  }

  getEvents(): EventInformation[] {
    this.getEventsObservable().subscribe(eventInformation => {
      
      for (var key in eventInformation[0]) {
        console.log(`element: ${key}: ${eventInformation[0][key]}`);
        
      }
      for (var counter in eventInformation) {
        this.events.push(EventInformation.fromObject(eventInformation[counter]))
      }
      console.log(`events: ${this.events}`)
      for (var key in this.events) {
        console.log(`element: ${key}: ${this.events[key]}`);
        console.log(`element: ${key}: ${this.events[key].creator}`);

        console.log(`element: ${key}: ${this.events[0][key]}`);
      }
    })
    
    return this.events;
  }
}
