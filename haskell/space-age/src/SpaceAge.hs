module SpaceAge (Planet (..), ageOn) where

data Planet
  = Mercury
  | Venus
  | Earth
  | Mars
  | Jupiter
  | Saturn
  | Uranus
  | Neptune

ageOn :: Planet -> Float -> Float
ageOn planet seconds = secondsInEarthYears / planetToEarthYearRatio planet
  where
    oneEarthYearInSeconds = 31557600
    secondsInEarthYears = seconds / oneEarthYearInSeconds
    planetToEarthYearRatio :: Planet -> Float
    planetToEarthYearRatio Mercury = 0.2408467
    planetToEarthYearRatio Venus = 0.61519726
    planetToEarthYearRatio Earth = 1
    planetToEarthYearRatio Mars = 1.8808158
    planetToEarthYearRatio Jupiter = 11.862615
    planetToEarthYearRatio Saturn = 29.447498
    planetToEarthYearRatio Uranus = 84.016846
    planetToEarthYearRatio Neptune = 164.79132
