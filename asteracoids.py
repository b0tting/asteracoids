from lib.gameconfig import GameConfig
from lib.gamesetup import GameSetup

if __name__ == "__main__":
    game_config = GameConfig()
    game_setup = GameSetup(game_config)
    game_setup.run()