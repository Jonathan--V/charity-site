import { StrStrMap } from './types';

export class Store{
  
  constructor(private prefix: string) {}

  public setItem(item: string, value: string): void {
    localStorage[this.prefix + item] = value
  }

  public getItem(item: string): string | undefined {
    return localStorage[this.prefix + item]
  }

  public clear(): void {
    for (let key in localStorage) {
      if (key.startsWith(this.prefix)) {
        localStorage.removeItem(key)
      }
    }
  }

  public load(): StrStrMap {
    let matches: StrStrMap = {}
    for (let key in localStorage) {
      if (key.startsWith(this.prefix)) {
        matches[key.substring(this.prefix.length)] = String(localStorage.getItem(key))
      }
    }
    return matches
  }
}