import pygame

from lib.asteroid import Asteroid
from lib.player import Player

class AsteracoidsGame:
    def __init__(self, gameconfig):
        self.gameconfig = gameconfig
        self.restart()

    def restart(self):
        self.missiles = pygame.sprite.Group()
        player_sprite = Player(self.gameconfig, self.missiles)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.asteroids = pygame.sprite.Group()
        for number in range(self.gameconfig.asteroids_level_1):
            Asteroid(self.asteroids,
                     self.gameconfig,
                     self.player.sprite.rect,
                     self.gameconfig.asteroid_default_layers
                    )

    def updates(self):
        self.asteroids.update()
        self.missiles.update()
        self.player.update()
        self.check_collisions()

    def draws(self, screen):
        self.asteroids.draw(screen)
        self.missiles.draw(screen)
        self.player.sprite.draw_extended(screen)

    def check_collision(self, left, right, use_accurate=True):
        if use_accurate:
            return pygame.sprite.collide_mask(left, right)
        else:
            return pygame.sprite.collide_rect(left, right)

    def check_collisions(self):
        dead = False

        # Collision detection is done asteroid first. This is currently done using the
        # "collide_mask" method. That might be expensive, so there is a switch to allow fallback
        # to the less accurate rect collision detection
        use_accurate = self.gameconfig.detailed_collisions
        for asteroid in self.asteroids.sprites():

            # First, check collisions with the player
            if self.check_collision(asteroid, self.player.sprite, use_accurate):
                dead = True
                break

            # Next, check for missile hits
            for missile in self.missiles.sprites():
                if self.check_collision(asteroid, missile, use_accurate):
                    asteroid.handle_hit()
                    missile.kill()

            # Next check if another asteroid hit us
            for asteroid_boink in self.asteroids.sprites():
                if asteroid_boink is not asteroid:
                    if self.check_collision(asteroid, asteroid_boink, False):
                        asteroid.bounce(asteroid_boink)

        if dead:
            self.restart()

        if not self.asteroids.sprites():
            self.restart()


