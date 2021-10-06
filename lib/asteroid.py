import random

import pygame

from lib.mobile import Mobile


class Asteroid(Mobile):
    random_angles = list(range(15, 80)) + list(range(115, 165)) + list(range(195, 255)) + list(range(290, 335))

    def __init__(self, gameconfig, player_rect):
        self.player_rect = player_rect
        self.imagename = random.choice(["resources/asteroid1.png",
                                        "resources/asteroid2.png",
                                        "resources/asteroid3.png"])
        self.scale = random.randint(gameconfig.asteroid_min_scale,
                                    gameconfig.asteroid_max_scale)
        super().__init__(gameconfig)
        self.image = pygame.transform.rotate(self.image, self.get_random_angle())
        self.speed = random.uniform(gameconfig.asteroid_min_speed,
                                    gameconfig.asteroid_max_speed)

    # Does nothing here, but allows for correction in subclasses
    def fix_boring_angles(self, old_pos, new_pos):
        x = new_pos[0]
        if old_pos[0] == x:
            x += 1
        y = new_pos[1]
        if old_pos[1] == y:
            y -= 1
        return x, y

    def get_random_angle(self, no_boring=False):
        # We need to prevent boring angles like 0, 90, etc.
        if no_boring:
            return random.choice(Asteroid.random_angles)
        else:
            return random.randint(0, 360)

    def get_starting_pos(self):
        # We need to get a location away from the player pos
        start_point = self.player_rect.center

        # Take a random angle point that way. Set this as the direction for our asteroid
        angle = self.get_random_angle(no_boring=True)
        self.angle = angle

        # This code is not entirely correct if we are not in an exact square screen,
        # but we need to find a nice distance away from the player and not go to far or we'll wrap
        # around the screen and hit the player. We first need the smaller of width or height of the screen
        max_distance = self.gameconfig.screen_width if self.gameconfig.screen_width < self.gameconfig.screen_height\
            else self.gameconfig.screen_height

        # Pick a random length
        distance = random.randint(self.gameconfig.asteroid_spawn_distance,
                                  max_distance - self.gameconfig.asteroid_spawn_distance)

        # Calculate the point that far away from the player at the chosen angle
        pos = pygame.math.Vector2()
        pos.from_polar((distance, angle))
        pos = start_point + pos

        # Use the modulo operator to prevent being thrown out of the screen
        pos = pos[0] % self.gameconfig.screen_width, pos[1] % self.gameconfig.screen_width
        return pos

    def update(self):
        self.set_new_position()
