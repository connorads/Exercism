export default class Clock {
  readonly hour: number;
  readonly minute: number;

  constructor(hour: number, minute = 0) {
    const additionalHours = Math.floor(minute / 60);
    this.hour = (24 + ((hour + additionalHours) % 24)) % 24;
    this.minute = (60 + (minute % 60)) % 60;
  }

  toString = () => `${to2digits(this.hour)}:${to2digits(this.minute)}`;
  plus = (minute: number) => new Clock(this.hour, this.minute + minute);
  minus = (minute: number) => this.plus(-minute);
  equals = (c: Clock) => c.hour === this.hour && c.minute === this.minute;
}

const to2digits = (n: number) => n.toString().padStart(2, "0");
