export const gigasecond = (date) => {
  const oneGigasecondInMilliseconds = 1e12;
  return new Date(date.getTime() + oneGigasecondInMilliseconds);
};