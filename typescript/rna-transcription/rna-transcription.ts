class Transcriptor {
  private dnaToRnaMap = new Map([
    ["G", "C"],
    ["C", "G"],
    ["T", "A"],
    ["A", "U"]
  ]);

  toRna(dna: string): string {
    return Array.from(dna)
      .map(nucleotide => {
        if (!this.dnaToRnaMap.has(nucleotide)) {
          throw Error("Invalid input DNA.");
        }
        return this.dnaToRnaMap.get(nucleotide);
      })
      .join("");
  }
}

export default Transcriptor;
