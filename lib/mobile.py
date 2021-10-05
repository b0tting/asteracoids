import pygame


class Mobile(pygame.sprite.Sprite):
    imagename = None

    def __init__(self, gameconfig):
        super().__init__()
        self.gameconfig = gameconfig
        self.angle = 0
        self.speed = 0
        unscaled_image = pygame.image.load(self.imagename).convert_alpha()
        self.image = pygame.transform.smoothscale(unscaled_image, (self.scale, self.scale))
        self.rect = self.image.get_rect(center=self.get_starting_pos())

    def set_new_position(self):
        if self.speed > 0:
            pos = self.rect.center
            # https://stackoverflow.com/questions/46697502/how-to-move-a-sprite-according-to-an-angle-in-pygame
            move_vec = pygame.math.Vector2()
            move_vec.from_polar((self.speed, self.angle))
            new_x = pos[0] + move_vec[0]
            new_y = pos[1] - move_vec[1]
            self.rect.center = self.get_boundary_correct_pos(new_x, new_y)

    # This function takes your x and y and wraps those around the screen if required.
    # I leave a ghost area of half the size of your ship outside of the game bounds
    def get_boundary_correct_pos(self, x, y):
        if x > (self.gameconfig.screen_width + self.rect.width / 2):
            x = 0
        elif x < 0:
            x = self.gameconfig.screen_width
        if y > (self.gameconfig.screen_height + self.rect.height / 2):
            y = 0
        elif y < 0:
            y = self.gameconfig.screen_height
        return round(x), round(y)

    def get_starting_pos(self):
        return 0, 0

    def rotate_left(self, rotate_speed):
        self.rotate(rotate_speed, False)

    def rotate_right(self, rotate_speed):
        self.rotate(rotate_speed, True)

    def rotate(self, rotate_speed, rotate_right=False):
        if rotate_right:
            self.angle += (rotate_speed / 10)
        else:
            self.angle -= (rotate_speed / 10)
        self.angle %= 360

    def change_momentum(self):
        self.speed = self.speed - self.gameconfig.momentum_loss
        if self.speed < 0:
            self.speed = 0
