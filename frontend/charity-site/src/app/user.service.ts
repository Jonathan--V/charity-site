import { Injectable } from '@angular/core';
import { EventInformation } from './event-information';
import { Store } from './store';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  store = new Store('authentication.')

  constructor() {}
   
  public isLoggedIn(): boolean {
    const expirySeconds = this.store.getItem('token_expiry') || 0

    const hasJWT = !!this.getToken()
    const JWTNotExpired = +expirySeconds * 1000 > Date.now()
    const hasUsername = !!this.getUsername()
    return hasJWT && JWTNotExpired && hasUsername
  }

  public getToken(): string {
    return this.store.getItem('token') || ''
  }

  public getUsername(): string {
    return this.store.getItem('username') || ''
  }

  public canDelete(eventInformation: EventInformation): boolean {
    return this.isLoggedIn()
      && eventInformation.creator == this.getUsername()
  }

  public expiresSoon(): boolean {
    const expirySeconds = this.store.getItem('token_expiry') || 0
    const fiveMinutes = 300000
    return +expirySeconds * 1000 < Date.now() + fiveMinutes
  }

  public updateData(token: string): void {
    const token_parts = token.split(/\./)
    const token_decoded = JSON.parse(window.atob(token_parts[1]))
    this.store.setItem('token', token)
    this.store.setItem('token_expiry', token_decoded.exp)
    this.store.setItem('username', token_decoded.username)
  }

  public clearAuthenticationData() {
    this.store.clear()
  }


}
