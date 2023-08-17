"""Convert seconds to years on different planets in the solar system."""

from types import MethodType
from typing import Callable, Literal, Self

Planet = Literal[
    "earth", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"
]


SECONDS_IN_PLANET_YEAR: dict[Planet, float] = {
    "earth": 31557600,
    "mercury": 7600543.81992,
    "venus": 19414149.052176,
    "mars": 59354032.69008,
    "jupiter": 374355659.124,
    "saturn": 929292362.8848,
    "uranus": 2651370019.3296,
    "neptune": 5200418560.032001,
}


class SpaceAge:
    """Converts seconds to years on different planets in the solar system."""

    def __init__(self, seconds: int):
        self.seconds = seconds

        for planet, _ in SECONDS_IN_PLANET_YEAR.items():
            method = self._on_planet(planet)
            setattr(self, "on_" + planet, MethodType(method, self))

    def _on_planet(self, planet: Planet) -> Callable[[Self], float]:
        return lambda self: round(self.seconds / SECONDS_IN_PLANET_YEAR[planet], 2)
