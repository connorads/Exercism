export const toRna = dna => {
  return Array.from(dna)
    .map(nucleotide => {
      return dnaToRnaMap.get(nucleotide);
    })
    .join("");
};

const dnaToRnaMap = new Map([
  ["G", "C"],
  ["C", "G"],
  ["T", "A"],
  ["A", "U"]
]);
