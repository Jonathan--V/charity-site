import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from "src/app/user.service";
import { AuthenticationService } from '../authentication.service';
import { StrStrMap } from '../types';
import { Utility } from '../utility';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  returnUrl: string = '/';

  username: string = '';
  password: string = '';
  errors: StrStrMap = {};

  getUsernameError(): string{
	  return this.errors.username;
  }

  getPasswordError(): string{
	  return this.errors.password;
  }


  constructor(
    private userService: UserService,
    private authenticationService: AuthenticationService,
    private router: Router,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
    this.route.queryParams
      .subscribe(params => {
        this.returnUrl = params.returnUrl
      })
  }

  getOtherErrors(): string[] {
    let otherErrors = [];
    for (const [key, value] of Object.entries(this.errors)) {
      if (!['username', 'password'].includes(key)) {
        otherErrors.push(value);
      }
    }
    return otherErrors;
  }

  login() {
    this.authenticationService.loginObservable(this.username, this.password).subscribe(
      (data: StrStrMap) => {
        this.errors = {}
        this.userService.updateData(data['token']);
        this.router.navigate([this.returnUrl])
      },
      errorResponse => {
        this.errors = Utility.processErrorsMap(errorResponse, "Error when attempting to login")
      }
    )
  }
}