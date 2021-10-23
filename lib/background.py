import pygame

from lib.gameutils import GameUtils


class Background(pygame.sprite.Sprite):
    def __init__(self, gameconfig):
        super().__init__()
        self.gameconfig = gameconfig
        unscaled =  pygame.image.load("resources/paper_background.jpg")
        self.image = pygame.transform.smoothscale(unscaled,
                                                  (gameconfig.screen_width, gameconfig.screen_height))
        self.rect = self.image.get_rect(topleft=(0, 0))
