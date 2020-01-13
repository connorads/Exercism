export const age = (planet, seconds) => {
  const secondsInEarthYears = seconds / oneEarthYearInSeconds;
  const planetToEarthYearRatio = planetToEarthYearRatioMap.get(planet);
  const age = secondsInEarthYears / planetToEarthYearRatio;
  return Math.round(age * 100) / 100;
};

const oneEarthYearInSeconds = 31557600;

const planetToEarthYearRatioMap = new Map([
  ["earth", 1.0],
  ["mercury", 0.2408467],
  ["venus", 0.61519726],
  ["mars", 1.8808158],
  ["jupiter", 11.862615],
  ["saturn", 29.447498],
  ["uranus", 84.016846],
  ["neptune", 164.79132]
]);