import pygame

from lib.asteroid import Asteroid
from lib.player import Player

class AsteracoidsGame:
    def __init__(self, gameconfig):
        self.gameconfig = gameconfig
        player_sprite = Player(self.gameconfig)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.asteroids = pygame.sprite.Group()
        for numb in range(self.gameconfig.asteroids_level_1):
            self.asteroids.add(Asteroid(self.gameconfig, self.player.sprite.rect))

    def updates(self):
        self.asteroids.update()
        self.player.update()

    def draws(self, screen):
        self.asteroids.draw(screen)
        self.player.sprite.draw_extended(screen)
