from dataclasses import dataclass

@dataclass
class GameConfig:
    # Speed buildup for the player ship per frame
    player_speed: float = 0.1
    # Max speed for the player ship per frame
    player_max_speed: float = 10
    # Player turn speed
    player_rotate_speed: float = 20
    # Momentum loss
    momentum_loss: float = 0.05
    # Player image scale factor
    player_image_scale: int = 30
    # Asteroid minimal speed at zero level
    asteroid_min_speed: float = 0.6
    # Asteroid max speed at zero level
    asteroid_max_speed: float = 1.5
    # Asteroid minimal speed at zero level
    asteroid_min_scale: float = 70
    # Asteroid max speed at zero level
    asteroid_max_scale: float = 100
    # Asteroid minimum spawn distance from player
    asteroid_spawn_distance: int = 50
    # Asteroids spawning in level 1
    asteroids_level_1: int = 2
    screen_width: int = 600
    screen_height: int = 600
