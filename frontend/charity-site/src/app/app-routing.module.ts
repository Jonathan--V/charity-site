import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EventsComponent } from './events/events.component';
import { EventsDetailComponent } from "./events-detail/events-detail.component";
import { LoginComponent } from "src/app/login/login.component";
import { EventsCreationComponent } from "src/app/events-creation/events-creation.component";

const routes: Routes = [
  { path: '', redirectTo: 'events', pathMatch: 'full' },
  { path: 'events', component: EventsComponent },
  { path: 'events/create', component: EventsCreationComponent },
  { path: 'events/:id', component: EventsDetailComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
  
}
