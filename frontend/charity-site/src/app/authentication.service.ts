import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DrfCommunicationService } from './drf-communication.service';
import { StrStrMap } from './types';
import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private drfCommunicationService: DrfCommunicationService, private userService: UserService) { }

  public loginObservable(username: string, password: string): Observable<StrStrMap> {
    return this.drfCommunicationService.post('token-auth/', { username, password }, false)
  }

  /*
   * As we're using JWTs without a revoke list, the JWT is unavoidably still valid.
   * "Logging out" simply means the user will need to log in again and be reissued a JWT.
   * So, we do not need to contact the backend server.
   */
  public logout(): void {
    return this.userService.clearAuthenticationData()
  }
}