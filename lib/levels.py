from dataclasses import dataclass

class Levels:
    def __init__(self):
        self.levels = [LevelOne(), LevelTwo(), LevelThree(), LevelFour()]
        self.current = 0

    def get_next_level(self):
        level = self.levels[self.current]
        self.current += 1
        if self.current >= len(self.levels):
            self.current = 0
        return level

    def restart_levels(self):
        self.current = 0


@dataclass
class BaseLevel:
    # Asteroid minimal speed at zero level
    asteroid_min_speed: float = 0.6

    # Asteroid max speed at zero level
    asteroid_max_speed: float = 1.5

    # Asteroid minimal speed at zero level
    asteroid_min_scale: float = 100

    # Asteroid max speed at zero level
    asteroid_max_scale: float = 120

    # Asteroids spawning in level 1
    asteroids_spawning: int = 4

    # Default number of layers in an asteroid
    asteroid_default_layers: int = 2

    # Asteroid debris max speedup
    asteroid_debris_speedup: int = 1

    # Minimum number of pieces that spawn when an asteroid gets hit
    asteroid_min_pieces: int = 2

    # Maximum number of pieces that spawn when an asteroid gets hit
    asteroid_max_pieces: int = 5


@dataclass
class LevelOne(BaseLevel):
    asteroids_spawning: int = 1
    asteroid_default_layers: int = 1
    asteroid_min_pieces: int = 2
    asteroid_max_pieces: int = 3
    asteroid_min_scale: float = 200
    asteroid_max_scale: float = 220

@dataclass
class LevelTwo(BaseLevel):
    asteroids_spawning: int = 1
    asteroid_default_layers: int = 2
    asteroid_min_scale: float = 250
    asteroid_max_scale: float = 300
    asteroid_min_pieces: int = 6
    asteroid_max_pieces: int = 8
    asteroid_min_speed: float = 0.2
    asteroid_max_speed: float = 0.6

@dataclass
class LevelThree(BaseLevel):
    asteroids_spawning: int = 5
    asteroid_default_layers: int = 4
    asteroid_min_speed: float = 0.4
    asteroid_max_speed: float = 0.7

@dataclass
class LevelFour(BaseLevel):
    asteroids_spawning: int = 3
    asteroid_min_speed: float = 2
    asteroid_max_speed: float = 3
