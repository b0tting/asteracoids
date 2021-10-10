import random

import pygame

from lib.mobile import Mobile


class Asteroid(Mobile):
    def __init__(self, asteroids, level, game_config, start_pos, asteroid_depth,
                 speed=None, scale=None, evade_start_pos=True):
        self.asteroids = asteroids
        self.level = level
        self.gameconfig = game_config
        self.start_pos = start_pos
        self.evade_start_pos = evade_start_pos
        self.imagename = random.choice(["resources/asteroid1.png",
                                        "resources/asteroid2.png",
                                        "resources/asteroid3.png"])
        if not scale:
            self.scale = random.randint(level.asteroid_min_scale,
                                        level.asteroid_max_scale)
        else:
            self.scale = scale
        self.asteroid_depth = asteroid_depth
        super().__init__(self.gameconfig)
        self.image = pygame.transform.rotate(self.image, self.get_random_angle())
        if not speed:
            self.speed = random.uniform(level.asteroid_min_speed,
                                        level.asteroid_max_speed)
        else:
            self.speed = speed
        self.move_if_overlapping()
        self.last_boink = None
        self.asteroids.add(self)

    # An inaccurate way to prevent asteroid overlap on spawn
    def move_if_overlapping(self):
        while pygame.sprite.spritecollideany(self, self.asteroids):
            self.move_to(self.get_move_coordinates(self.rect.height, self.get_random_angle()))

    # Does nothing here, but allows for correction in subclasses
    def fix_boring_angles(self, old_pos, new_pos):
        x = new_pos[0]
        if old_pos[0] == x:
            x += 1
        y = new_pos[1]
        if old_pos[1] == y:
            y -= 1
        return x, y

    def get_random_angle(self):
        return random.randint(0, 3600) / 10

    def bounce(self, asteroid_boink):
        # IF asteroids boink I give them once chance to turn around. After that, I ignore
        # the bump so that the asteroids have time to drift apart again.
        if self.last_boink == asteroid_boink:
            pass
        else:
            self.last_boink = asteroid_boink
            self.angle = (self.angle + 90) % 360
            asteroid_boink.angle = (self.angle + 180) % 360

    def handle_hit(self):
        new_asteroids = []
        start_pos = self.rect.x, self.rect.y
        self.kill()
        if self.asteroid_depth > 0:
            num_pieces = random.randint(self.level.asteroid_min_pieces,
                                        self.level.asteroid_max_pieces)

            for num in range(num_pieces):
                speedup = self.speed + random.randint(0, self.level.asteroid_debris_speedup)
                scale = random.randint(self.scale // 3, self.scale // 2)
                Asteroid(self.asteroids,
                         self.level,
                         self.gameconfig,
                         start_pos,
                         self.asteroid_depth - 1,
                         speed=speedup,
                         scale=scale,
                         evade_start_pos=False)
        return new_asteroids

    def get_starting_pos(self):
        angle = self.get_random_angle()
        self.angle = angle
        # @todo: Not working if an asteroid explodes near the player. We should select angles
        # away from the player here
        if self.evade_start_pos:
            # We need to get a location away from the player pos
            start_point = self.start_pos.center

            # This code is not entirely correct if we are not in an exact square screen,
            # but we need to find a nice distance away from the player and not go to far or we'll wrap
            # around the screen and hit the player. We first need the smaller of width or height of the screen
            max_distance = self.gameconfig.screen_width if \
                self.gameconfig.screen_width < self.gameconfig.screen_height \
                else self.gameconfig.screen_height

            # Pick a random length
            distance = random.randint(self.gameconfig.asteroid_spawn_distance,
                                      max_distance - self.gameconfig.asteroid_spawn_distance)

            # Calculate the point that far away from the player at the chosen angle
            pos = self.get_move_coordinates(distance, angle, start_point)

            # Use the modulo operator to prevent being thrown out of the screen
            pos = pos[0] % self.gameconfig.screen_width, pos[1] % self.gameconfig .screen_width
        else:
            pos = self.start_pos
        return pos

    def get_score(self):
        points = self.gameconfig.score_asteroid_base
        points += round(self.gameconfig.score_asteroid_speedmult * self.speed)
        points += round(self.gameconfig.score_asteroid_scalemult * self.scale)
        return points


