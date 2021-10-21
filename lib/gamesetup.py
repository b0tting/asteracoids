import sys

import pygame

from lib.asteracoidsgame import AsteracoidsGameStateContext


# Game setup class handles all meta stuff like the canvas etc
class GameSetup:
    def __init__(self, gc):
        self.gameconfig = gc
        self.state = None
        self.screen = pygame.display.set_mode((gc.screen_width, gc.screen_height))
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.gameconfig.game_title)
        self.state = AsteracoidsGameStateContext(self.gameconfig)
        while True:
            self.loop()

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.state.updates()
        self.screen.fill((255, 255, 255))
        self.state.draws(self.screen)
        pygame.display.flip()
        self.clock.tick(60)
