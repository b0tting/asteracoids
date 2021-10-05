import pygame

from lib.mobile import Mobile

# Ready player one!
class Player(Mobile):
    def __init__(self, gameconfig):
        self.scale = gameconfig.player_image_scale
        self.imagename = "resources/player.png"
        super().__init__(gameconfig)

    def get_starting_pos(self):
        return self.gameconfig.screen_width / 2, self.gameconfig.screen_height / 2

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rotate_left(self.gameconfig.player_rotate_speed)
        elif keys[pygame.K_LEFT]:
            self.rotate_right(self.gameconfig.player_rotate_speed)
        if keys[pygame.K_UP]:
            self.add_speed(self.gameconfig.player_speed)

    def add_speed(self, speed):
        self.speed += speed
        if self.speed > self.gameconfig.player_max_speed:
            self.speed = self.gameconfig.player_max_speed

    def update(self):
        self.change_momentum()
        self.get_input()
        self.set_new_position()

    # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
    def draw_extended(self, screen):
        pos = (self.rect.x, self.rect.y)
        # offset from pivot to center
        image_rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(self.angle * -1)

        # rotated image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # rotate and blit the image
        screen.blit(rotated_image, rotated_image_rect)

