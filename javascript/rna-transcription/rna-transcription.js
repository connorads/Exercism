export const toRna = (dna) => {
  return Array.prototype.map.call(dna, char => {
    switch(char) {
      case 'G': return 'C';
      case 'C': return 'G';
      case 'T': return 'A';
      case 'A': return 'U';
    }
  }).join("");
};
