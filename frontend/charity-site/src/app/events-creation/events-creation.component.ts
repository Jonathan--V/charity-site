import { Component, OnInit } from '@angular/core';
import { EventService } from "src/app/event.service";
import { UserService } from "src/app/user.service";
import { StrStrMap } from '../types';
import { Utility } from '../utility';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-events-creation',
  templateUrl: './events-creation.component.html',
  styleUrls: ['./events-creation.component.css']

})
export class EventsCreationComponent implements OnInit {

  private model: StrStrMap = {}

  private errors: string[] = []

  private latestAddedId: string = ''
    

  constructor(private userService: UserService, private eventService: EventService, private router: Router) { }
  
  ngOnInit() {
    this.redirectToLogin()
  }

  public isLoggedIn(): boolean {
    return this.userService.isLoggedIn()
  }
  private redirectToLogin() {
    if (!this.isLoggedIn()) {
      this.router.navigate(['/login'], { queryParams: { returnUrl: this.router.url } })
    }
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
          this.latestAddedId = successfulResponse.id
        },
        errorResponse => {
          this.errors = Utility.processErrors(errorResponse, "Error when attempting to create event.")
        }
      )
    }
    
  }

}
