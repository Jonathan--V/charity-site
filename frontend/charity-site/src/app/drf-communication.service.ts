import { Injectable } from '@angular/core';
import { UserService } from './user.service';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from "rxjs";
import { StrStrMap } from './types';

@Injectable({
  providedIn: 'root'
})
export class DrfCommunicationService {

  constructor(private http: HttpClient, private userService: UserService) { }


  public get<T>(suffix: string): Observable<T> {
    return this.http.get<T>(this.buildUrl(suffix))
  }

  public post(suffix: string, body: StrStrMap, requiresAuthentication = true): Observable<StrStrMap> {
    const headers = requiresAuthentication ? this.getHeaders() : undefined
    return this.http.post<StrStrMap>(this.buildUrl(suffix), body, headers)
  }

  public delete(suffix: string) {
    return this.http.delete<StrStrMap>(this.buildUrl(suffix), this.getHeaders());
  }

  private getHeaders() {
    return {
      headers: new HttpHeaders({
        'Authorization': `JWT ${this.userService.getToken()}`

      })
    }
  }

  private getDRFUrl(): string {
    return "http://localhost:8000/en-gb/events/api/"
  }

  private buildUrl(suffix: string): string {
    return this.getDRFUrl() + suffix
  }
}
