export const isPangram = input => {
  input = input.toLowerCase();
  return [..."abcdefghijklmnopqrstuvwxyz"].every(letter =>
    input.includes(letter)
  );
};
