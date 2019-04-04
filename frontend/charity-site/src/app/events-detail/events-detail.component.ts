import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { EventInformation } from "src/app/event-information";
import { EventService } from "src/app/event.service";
import { StrStrMap, ErrorResponse } from "src/app/types";
import { Utility } from 'src/app/utility';
import { UserService } from '../user.service';

@Component({
  selector: 'app-events-detail',
  templateUrl: './events-detail.component.html',
  styleUrls: ['./events-detail.component.css']
})
export class EventsDetailComponent implements OnInit {
  event: EventInformation
  notices: string[] = []

  constructor(
    private eventService: EventService,
    private route: ActivatedRoute,
    private userService: UserService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.getEvent();
  }

  getEvent(): void {
    const id = this.route.snapshot.paramMap.get('id') || ''
    this.eventService.getEventObservable(id).subscribe(
      (eventResponse: StrStrMap) => 
        this.event = EventInformation.fromObject(eventResponse),
      (errorResponse: ErrorResponse) =>
        this.notices = Utility.processErrors(errorResponse, `Error when retrieving event with id ${id}`)
    )
  }

  canDelete(): boolean {
    return this.userService.canDelete(this.event)
  }

  deleteEvent(): void {
    this.eventService.deleteEvent(this.event, this.notices, () => this.router.navigate(['/events/']), () => { })
  }

}