"""Solution to Ellen's Alien Game exercise."""

from typing import Self


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        """Initialize Alien object."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self) -> bool:
        """Return a boolean for if Alien is alive (if health is > 0)."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, _: Self) -> None:
        """Implementation TBD."""


def new_aliens_collection(coordinates: list[tuple[int, int]]) -> list[Alien]:
    """Create a list of Alien objects with coordinates from a list of tuples."""
    return [Alien(*coordinate) for coordinate in coordinates]
