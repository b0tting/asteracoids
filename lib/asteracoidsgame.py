import pygame

from lib.player import Player


class AsteracoidsGame:
    def __init__(self, gameconfig):
        self.gameconfig = gameconfig
        player_sprite = Player(self.gameconfig)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def updates(self):
        self.player.update()


    def draws(self, screen):
        self.player.draw(screen)