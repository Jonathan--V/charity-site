import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { EventInformation } from "src/app/event-information";
import { Observable } from "rxjs";
import { ActivatedRoute } from "@angular/router";


@Component({
  selector: 'app-events-detail',
  templateUrl: './events-detail.component.html',
  styleUrls: ['./events-detail.component.css']
})
export class EventsDetailComponent implements OnInit {
  eventDetailUrl: string = "http://localhost:8000/en-gb/events/api/events/";
  event: EventInformation;

  constructor(private http: HttpClient, private route: ActivatedRoute,) { }

  ngOnInit(): void {
    this.getEvent();
  }

  getEventObservable(): Observable<EventInformation[]> {
    const id = this.route.snapshot.paramMap.get('id');
    return this.http.get<EventInformation[]>(this.eventDetailUrl + id)
  }

  getEvent(): void {
    this.getEventObservable().subscribe(eventInformation => {

      for (var key in eventInformation) {
        console.log(`element: ${key}: ${eventInformation[key]}`);

      }
      this.event = EventInformation.fromObject(eventInformation);
      console.log(`event: ${this.event}`)
      for (var key in this.event) {
        console.log(`element: ${key}: ${this.event[key]}`);
        
      }
    })
  }
}
