import { Component, OnInit } from '@angular/core';
import { EventService } from "src/app/event.service";
import { UserService } from "src/app/user.service";
import { StrStrMap } from '../types';
import { Utility } from '../utility';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Store } from '../store';

@Component({
  selector: 'app-events-creation',
  templateUrl: './events-creation.component.html',
  styleUrls: ['./events-creation.component.css']

})
export class EventsCreationComponent implements OnInit {

  private model: StrStrMap = {}

  private errors: string[] = []

  private latestAddedId: string = ''

  private store = new Store("event-creation-form.")

  constructor(private userService: UserService, private eventService: EventService, private router: Router) { }
  
  ngOnInit() {
    if (!this.isLoggedIn()) {
      this.redirectToLogin()
    }
    else {
      this.load()
    }
  }

  public isLoggedIn(): boolean {
    return this.userService.isLoggedIn()
  }

  public createEvent(eventForm: NgForm): void {
    if (!this.userService.isLoggedIn()) {
      this.redirectToLogin()
    }
    else {
      this.model["creator"] = this.userService.getUsername();

      this.eventService.postEventObservable(this.model).subscribe(
        successfulResponse => {
          this.model = {}
          eventForm.reset()
          this.store.clear()
          this.latestAddedId = successfulResponse.id
        },
        errorResponse => {
          this.errors = Utility.processErrors(errorResponse, "Error when attempting to create event.")
        }
      )
    }
  }

  private redirectToLogin() {
    this.router.navigate(['/login'], { queryParams: { returnUrl: this.router.url } })
  }

  private save(field_name: string): void {
    this.store.setItem(field_name, this.model[field_name])
  }

  private load(): void {
    this.model = this.store.load()
  }



}
