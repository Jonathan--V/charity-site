import { HttpClient } from "@angular/common/http";
import { Injectable } from '@angular/core';
import { StrStrMap } from "src/app/types";
import { Utility } from './utility';
import { Observable } from 'rxjs';
import { EventInformation } from './event-information';


@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(private http: HttpClient) { }


  public loginObservable(username: string, password: string): Observable<StrStrMap> {
    return this.http.post <StrStrMap>('http://localhost:8000/en-gb/events/api/token-auth/', { username, password })
  }

  public isLoggedIn(): boolean {
    const expirySeconds = localStorage.getItem('token_expiry') || 0

    const hasJWT = !!this.getToken()
    const JWTNotExpired = +expirySeconds * 1000 > Date.now()
    const hasUsername = !!this.getUsername()
    return hasJWT && JWTNotExpired && hasUsername
  }

  public getToken(): string {
    return localStorage.getItem('token') || ''
  }

  public getUsername(): string {
    return localStorage.getItem('username') || ''
  }

  /*
   * As we're using JWTs without a revoke list, the JWT is unavoidably still valid.
   * "Logging out" simply means the user will need to log in again and be reissued a JWT.
   * So, we do not need to contact the backend server.
   */
  public logOut(): void {
    localStorage.clear()
  }

  public canDelete(eventInformation: EventInformation): boolean {
    return this.isLoggedIn()
      && eventInformation.creator == this.getUsername()
  }

  public updateData(token: string): void {
    const token_parts = token.split(/\./);

    const token_decoded = JSON.parse(window.atob(token_parts[1]));

    
    localStorage.setItem('token', token);
    localStorage.setItem('token_expiry', token_decoded.exp);

    localStorage.setItem('username', token_decoded.username);


  }
}
