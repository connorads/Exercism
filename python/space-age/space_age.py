"""Convert seconds to years on different planets in the solar system."""

from typing import Literal

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

    def _on_planet(self, planet: Planet) -> float:
        return round(self.seconds / SECONDS_IN_PLANET_YEAR[planet], 2)

    def on_earth(self) -> float:
        """Return the age in Earth years"""
        return self._on_planet("earth")

    def on_mercury(self) -> float:
        """Return the age in Mercurary years"""
        return self._on_planet("mercury")

    def on_venus(self) -> float:
        """Return the age in Venus years"""
        return self._on_planet("venus")

    def on_mars(self) -> float:
        """Return the age in Mars years"""
        return self._on_planet("mars")

    def on_jupiter(self) -> float:
        """Return the age in Jupiter years"""
        return self._on_planet("jupiter")

    def on_saturn(self) -> float:
        """Return the age in Saturn years"""
        return self._on_planet("saturn")

    def on_uranus(self) -> float:
        """Return the age in Uranus years"""
        return self._on_planet("uranus")

    def on_neptune(self) -> float:
        """Return the age in Neptune years"""
        return self._on_planet("neptune")
