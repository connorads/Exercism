export default class Pangram {
  constructor(private sentence: string) {}

  isPangram(): boolean {
    this.sentence = this.sentence.toLowerCase();
    return [..."abcdefghijklmnopqrstuvwxyz"].every(letter =>
      this.sentence.includes(letter)
    );
  }
}
