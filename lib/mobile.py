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
            new_x, new_y = self.get_move_coordinates(self.speed, self.angle)
            new_pos = self.get_boundary_correct_pos(new_x, new_y)
            new_pos = self.fix_boring_angles(pos, new_pos)
            self.rect.center = new_pos

    # Does nothing here, but allows for correction in subclasses
    def fix_boring_angles(self, old_pos, new_pos):
        return new_pos

    def get_move_coordinates(self, length, angle, pos=None):
        if not pos:
            pos = self.rect.center
        move_vec = pygame.math.Vector2()
        move_vec.from_polar((length, angle))
        new_x = pos[0] + move_vec[0]
        new_y = pos[1] - move_vec[1]
        return new_x, new_y

    def move_to(self, pos):
        self.rect.center = pos

    # This function takes your x and y and wraps those around the screen if required.
    # I leave a ghost area of half the size of your ship outside of the game bounds
    def get_boundary_correct_pos(self, x, y):
        half_height = self.rect.height / 2
        half_width = self.rect.width / 2
        if x > (self.gameconfig.screen_width + self.rect.width):
            x = 0 - half_width
        elif x + self.rect.width < 0:
            x = self.gameconfig.screen_width + half_width
        if y > (self.gameconfig.screen_height + self.rect.height):
            y = 0 - half_height
        elif y + self.rect.height < 0:
            y = self.gameconfig.screen_height + half_height
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

    def update(self):
        self.set_new_position()