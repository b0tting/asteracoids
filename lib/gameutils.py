class GameUtils:

    @staticmethod
    # This could be done with the Screen object as this also
    # has a rect, but I have the gameconfig *everywhere* and screen
    # only exists in the states
    def get_center_pos(gameconfig):
        return (gameconfig.screen_width // 2,
                     gameconfig.screen_height // 2)

