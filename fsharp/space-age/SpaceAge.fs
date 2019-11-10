module SpaceAge

type Planet =
    | Earth
    | Mercury
    | Venus
    | Mars
    | Jupiter
    | Saturn
    | Uranus
    | Neptune

let age (planet: Planet) (seconds: int64): float =
    let oneEarthYearInSeconds = (float) 31557600
    let secondsInEarthYears = (float) seconds / oneEarthYearInSeconds
    match planet with
    | Earth -> secondsInEarthYears
    | Mercury -> secondsInEarthYears / 0.2408467
    | Venus -> secondsInEarthYears / 0.61519726
    | Mars -> secondsInEarthYears / 1.8808158
    | Jupiter -> secondsInEarthYears / 11.862615
    | Saturn -> secondsInEarthYears / 29.447498
    | Uranus -> secondsInEarthYears / 84.016846
    | Neptune -> secondsInEarthYears / 164.79132