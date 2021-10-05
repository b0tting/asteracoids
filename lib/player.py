import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, gameconfig):
        super().__init__()
        self.gameconfig = gameconfig
        unscaled_image = pygame.image.load("resources/player.png").convert_alpha()
        self.image = pygame.transform.smoothscale(unscaled_image, (64, 64))
        self.rect = self.image.get_rect(midbottom=self.get_starting_pos())

    def get_starting_pos(self):
        return self.gameconfig.screen_width / 2, self.gameconfig.screen_height / 2

    def get_current_speed(self):
        return self.gameconfig.player_speed

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.get_current_speed()
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.get_current_speed()

    def update(self):
        self.get_input()
