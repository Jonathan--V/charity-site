import { Component, OnInit, Input } from '@angular/core';
import { UserService } from "src/app/user.service";
import { StrStrMap } from '../types';
import { Utility } from '../utility';
import { Router, ActivatedRoute } from '@angular/router';

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

  usernameErrors: string = this.errors['username'];

  passwordErrors: string = this.errors['password'];


  constructor(private userService: UserService, private router: Router, private route: ActivatedRoute) { }


  ngOnInit() {
    this.route.queryParams
      .subscribe(params => {
        console.log(params)
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
    this.userService.loginObservable(this.username, this.password).subscribe(
      (data: StrStrMap) => {
        this.errors = {}
        this.userService.updateData(data['token']);
        this.router.navigate([this.returnUrl])
      },
      errorResponse => {
        this.errors = Utility.processErrorsMap(errorResponse, "Error when attempting to login:")
      }
    )
  }


  //refreshToken() {
  //  this.userService.refreshToken();

  //}

  //logout() {
  //  this.userService.logout();

  //}

    
}
