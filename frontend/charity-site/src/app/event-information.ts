import { StrStrMap } from "src/app/types";

export class EventInformation{
  private constructor(
    public readonly creator: string,
    public readonly date: Date,
    public readonly description: string,
    public readonly location: string,
    public readonly name: string,
    public readonly id?: number,
  ) { }

  public toString(): string {
    if (!this.date) {
      return "Event not yet loaded."
    }
    else{
      return `${this.name} - ${this.date.toString()}`
    }
  }

  public static fromObject(eventInformation: StrStrMap): EventInformation {
    //Essentially want to do:
        //new EventInformation(...eventInformation));
        //Spelt out:
    return new EventInformation(
        eventInformation["creator"],
        new Date(eventInformation["date"]),
        eventInformation["description"],
        eventInformation["location"],
        eventInformation["name"],
        +eventInformation["id"],
    )
  }
}