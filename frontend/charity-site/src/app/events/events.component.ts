import { Component, OnInit } from '@angular/core';
import { EventInformation } from "src/app/event-information";
import { EventService } from "src/app/event.service";
import { Utility } from '../utility';
import { ErrorResponse, StrStrMap } from '../types';
import { UserService } from '../user.service';
import { AuthenticationService } from '../authentication.service';



@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  events: EventInformation[]

  notices: string[] = []

  constructor(private eventService: EventService, private userService: UserService, private authenticationService: AuthenticationService) { }


  ngOnInit(): void {
    this.updateEvents()
  }

  updateEvents(): void {
    this.eventService.getEventsObservable().subscribe(
      eventInformation => {
        this.events = []
        for (let counter in eventInformation) {
          this.events.push(EventInformation.fromObject(eventInformation[counter]))
        }
      },
      (errorResponse: ErrorResponse) => {
        this.notices = Utility.processErrors(errorResponse, "Error when retrieving events")
      }
    )
  }

  canDelete(eventInformation: EventInformation): boolean {
    return this.userService.canDelete(eventInformation)
  }

  deleteEvent(eventInformation: EventInformation): void {
    let update = () => this.updateEvents()
    this.eventService.deleteEvent(eventInformation, this.notices, update, update)
  }
}
