import { Injectable } from '@angular/core';
import { EventInformation } from './event-information';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() {}
   
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

  public canDelete(eventInformation: EventInformation): boolean {
    return this.isLoggedIn()
      && eventInformation.creator == this.getUsername()
  }

  public updateData(token: string): void {
    const token_parts = token.split(/\./)
    const token_decoded = JSON.parse(window.atob(token_parts[1]))
    localStorage.setItem('token', token)
    localStorage.setItem('token_expiry', token_decoded.exp)
    localStorage.setItem('username', token_decoded.username)
  }
}
