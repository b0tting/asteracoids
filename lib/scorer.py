import pygame


class Scorer(pygame.sprite.Sprite):
    def __init__(self, gameconfig):
        super().__init__()
        self.gameconfig = gameconfig
        self.fontsize = self.gameconfig.score_font_size
        self.font = pygame.font.SysFont("Arial", self.fontsize)
        self.rendered = None
        self.render("0")
        self.last_score = 0
        self.score = 0
        self.pos = self.get_score_location()

    def get_score_location(self):
        center = self.gameconfig.screen_width // 2
        return self.rendered.get_rect(midtop=(center, 10))

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)

    def update(self):
        # I read that rendering text is CPU expensive, so I update my render only
        # when the score changed this frame
        if self.score != self.last_score:
            self.last_score = self.score
            self.render(self.score)

    def add_points(self, points):
        self.score += points

    def render(self, text):
        text = str(text).zfill(5)
        self.rendered = self.font.render(str(text), True, (45, 49, 97))
