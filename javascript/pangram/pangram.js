export const isPangram = input => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const inputLowercase = input.toLowerCase();
  for (let i = 0; i < alphabet.length; i++) {
    if (inputLowercase.indexOf(alphabet[i]) == -1) return false;
  }
  return true;
};
