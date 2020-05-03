const alphabet = [..."abcdefghijklmnopqrstuvwxyz"];

export default class Pangram {
  constructor(private sentence: string) {}

  isPangram(): boolean {
    this.sentence = this.sentence.toLowerCase();
    return alphabet.every((letter) => this.sentence.includes(letter));
  }
}
