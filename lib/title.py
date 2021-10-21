import pygame

from lib.gameutils import GameUtils


class Title(pygame.sprite.Sprite):
    def __init__(self, gameconfig):
        super().__init__()
        self.imagename = "resources/title.png"
        self.gameconfig = gameconfig
        unscaled = pygame.image.load(self.imagename).convert_alpha()
        self.image = pygame.transform.smoothscale(unscaled,
                                                  (600,200))
        start_pos = GameUtils.get_center_pos(gameconfig)
        self.rect = self.image.get_rect(center=start_pos)

