import random

import pygame

from lib.mobile import Mobile

class Missile(Mobile):
    def __init__(self, gameconfig, angle, start_pos):
        self.start_pos = start_pos
        self.imagename = "resources/missile.png"
        self.scale = gameconfig.missile_scale
        super().__init__(gameconfig)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, angle)
        self.speed = self.gameconfig.missile_speed
        self.creation_time = pygame.time.get_ticks()

    def get_starting_pos(self):
        return self.start_pos

    def update(self):
        if self.creation_time + self.gameconfig.missile_life < pygame.time.get_ticks():
            self.kill()
        else:
            self.set_new_position()
