import { Injectable } from '@angular/core';
import { Observable } from "rxjs";
import { StrStrMap, ErrorResponse } from "src/app/types";
import { DrfCommunicationService } from './drf-communication.service';
import { EventInformation } from './event-information';
import { Utility } from './utility';

@Injectable({
  providedIn: 'root'
})
export class EventService {
    eventsUrlSuffix: string = "events/"

  constructor(private drfCommunicationService: DrfCommunicationService) { }


    getEventsObservable(): Observable<StrStrMap[]> {
      return this.drfCommunicationService.get(this.eventsUrlSuffix)

    }

    getEventObservable(id: string): Observable<StrStrMap> {
      return this.drfCommunicationService.get(this.eventsUrlSuffix + id)

    }

  postEventObservable(body: StrStrMap): Observable<StrStrMap> {
    return this.drfCommunicationService.post(this.eventsUrlSuffix, body)
  }

  deleteEventObservable(id: string): Observable<StrStrMap> {
    return this.drfCommunicationService.delete(this.eventsUrlSuffix + id)
  }

  deleteEvent(
    eventInformation: EventInformation,
    notices: string[],
    successfullCallback: () => void,
    unsuccessfullCallback: () => void): void {
    if (confirm(`Are you sure you want to delete ${eventInformation}?`)) {
      this.deleteEventObservable(String(eventInformation.id)).subscribe(
        () => {
          notices.push(`Succesfully deleted event ${eventInformation}`)
          successfullCallback()
        },
        (errorResponse: ErrorResponse) => {
          notices.push(...Utility.processErrors(errorResponse, `Error when deleting event with id ${eventInformation.id}`))
          unsuccessfullCallback()
        }
      )
    }
  }
}
