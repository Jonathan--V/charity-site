import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  constructor(
    private userService: UserService,
    private router: Router,
    private authenticationService: AuthenticationService
  ) { }

  ngOnInit() {
  }

  login_page(): void {
    this.router.navigate(['/login'], { queryParams: { returnUrl: this.router.url } });
  }

  isLoggedIn(): boolean {
    return this.userService.isLoggedIn()
  }

  getUsername(): string {
    return this.userService.getUsername()
  }

  logout(): void {
    this.authenticationService.logout()
  }
}
