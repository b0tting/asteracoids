import pygame


class TextRender(pygame.sprite.Sprite):
    def __init__(self, gameconfig, text, pos):
        super().__init__()
        self.gameconfig = gameconfig
        self.fontsize = self.gameconfig.score_font_size
        self.font = pygame.font.SysFont("Arial", self.fontsize)
        self.update(text)
        self.pos = self.rendered.get_rect(midtop=pos)

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)

    def update(self, text):
        self.rendered = self.font.render(str(text), True, (45, 49, 97))
