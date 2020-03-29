export default class Pangram {
  constructor(private input: string) {}

  isPangram(): boolean {
    this.input = this.input.toLowerCase();
    return [..."abcdefghijklmnopqrstuvwxyz"].every(letter =>
      this.input.includes(letter)
    );
  }
}
