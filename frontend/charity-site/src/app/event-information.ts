export class EventInformation{
  constructor(public creator,
    public date: Date,
    public description: string,
    public id: number,
    public location: string,
    public name: string) { }

  toString(): string {
    if (!this.date) {
      return "Event not yet loaded."
    }
    else{
      return `${this.name} - ${this.date.toString()}`
    }
  }

  static fromObject(eventInformation: object): EventInformation {
    //Essentially want to do:
        //new EventInformation(...eventInformation));
        //Spelt out:
    return new EventInformation(
        eventInformation["creator"],
        eventInformation["date"],
        eventInformation["description"],
        eventInformation["id"],
        eventInformation["location"],
        eventInformation["name"],
    )
  }
}
