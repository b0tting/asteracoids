import pygame

from lib.asteroid import Asteroid
from lib.player import Player

class AsteracoidsGame:
    def __init__(self, gameconfig):
        self.gameconfig = gameconfig
        self.restart()

    def restart(self):
        player_sprite = Player(self.gameconfig)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.asteroids = pygame.sprite.Group()
        for numb in range(self.gameconfig.asteroids_level_1):
            self.asteroids.add(Asteroid(self.gameconfig, self.player.sprite.rect))

    def updates(self):
        self.asteroids.update()
        self.player.update()
        self.check_collisions()

    def draws(self, screen):
        self.asteroids.draw(screen)
        self.player.sprite.draw_extended(screen)


    def check_collisions(self):
        dead = False


        for asteroid in self.asteroids.sprites():
            if pygame.sprite.collide_mask(asteroid, self.player.sprite):
                dead = True
                break
            for asteroid_boink in self.asteroids.sprites():
                if asteroid_boink is not asteroid:
                    if pygame.sprite.collide_mask(asteroid, asteroid_boink):
                        # Faking a correct bounce by rotating our asteroid an extra 90 degrees
                        asteroid.angle = (asteroid.angle + 90) % 360

        if dead:
            self.restart()

