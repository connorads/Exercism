class Transcriptor {
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

  private dnaToRnaMap = new Map([
    ["G", "C"],
    ["C", "G"],
    ["T", "A"],
    ["A", "U"]
  ]);
}

export default Transcriptor;
