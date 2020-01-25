export default class SpaceAge {
  readonly seconds: number;

  constructor(ageInSeconds: number) {
    this.seconds = ageInSeconds;
  }

  onEarth(): number {
    return this.getAge(1.0);
  }
  onMercury(): number {
    return this.getAge(0.2408467);
  }
  onVenus(): number {
    return this.getAge(0.61519726);
  }
  onMars(): number {
    return this.getAge(1.8808158);
  }
  onJupiter(): number {
    return this.getAge(11.862615);
  }
  onSaturn(): number {
    return this.getAge(29.447498);
  }
  onUranus(): number {
    return this.getAge(84.016846);
  }
  onNeptune(): number {
    return this.getAge(164.7913);
  }

  private getAge(planetToEarthYearRatio: number): number {
    const oneEarthYearInSeconds = 31557600;
    const ageInEarthYears = this.seconds / oneEarthYearInSeconds;
    const age = ageInEarthYears / planetToEarthYearRatio;
    return Math.round(age * 100) / 100;
  }
}
