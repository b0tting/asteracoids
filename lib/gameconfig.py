from dataclasses import dataclass

@dataclass
class GameConfig:
    # Speed buildup for the player ship per frame
    player_speed: int = 5
    # Max speed for the player ship per frame
    player_max_speed: int = 30

    screen_width: int = 600
    screen_height: int = 600
