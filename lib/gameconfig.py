from dataclasses import dataclass

@dataclass
class GameConfig:
    game_title: str = "Asteracoids!"
    # Use detailed collision detection. Works fine on my overpowered desktop but
    # might not work on potato computers.
    detailed_collisions: bool = True

    # Speed buildup for the player ship per frame
    player_speed: float = 0.1

    # Max speed for the player ship per frame
    player_max_speed: float = 20

    # Player turn speed
    player_rotate_speed: float = 20

    # Momentum loss
    momentum_loss: float = 0.05

    # Player image scale factor
    player_image_scale: int = 120

    # Player shot delay value, ie. how many ticks
    player_shot_delay: int = 1200

    # Missile also has a scale
    missile_scale: int = 10

    # Missile speed
    missile_speed: int = 5

    # Missile lifetime in MS
    missile_life: int = 2000

    # Asteroid minimum spawn distance from player
    asteroid_spawn_distance: int = 50

    # Font size for the score
    score_font_size: int = 64

    # Every asteroid has a base score with some multipliers
    score_asteroid_base: int = 100

    # Speed multi, this adds speed * speedmult to the score
    score_asteroid_speedmult: float = 3

    # Scale multi, this adds scale (size) to the score
    score_asteroid_scalemult: float = 1


    screen_width: int = 1000
    screen_height: int = 1000
