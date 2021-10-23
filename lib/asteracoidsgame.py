import pygame

from lib.asteroid import Asteroid
from lib.background import Background
from lib.gameutils import GameUtils
from lib.levels import Levels, LevelThree
from lib.player import Player
from lib.scorer import Scorer
from lib.textrender import TextRender
from lib.title import Title


# https://en.wikipedia.org/wiki/State_pattern
class AsteracoidsGameStateContext:
    def __init__(self, gameconfig):
        self.gameconfig = gameconfig
        self.set_state(AsteracoidsStateTitle(gameconfig, self))

    def updates(self):
        self.state.updates()

    def draws(self, screen):
        self.state.draws(screen)

    def set_state(self, state):
        self.state = state
        self.state.start_state()


class AsteracoidsState:
    def __init__(self, gameconfig, context):
        self.gameconfig = gameconfig
        self.context = context
        self.creation_time = pygame.time.get_ticks()
        background = Background(gameconfig)
        self.background = pygame.sprite.GroupSingle(background)

    def draws(self, screen):
        self.background.draw(screen)

class AsteracoidsStateRunning(AsteracoidsState):
    def start_state(self):
        self.levels = Levels()
        self.score = pygame.sprite.GroupSingle(Scorer(self.gameconfig))
        self.next_level()

    def next_level(self):
        level = self.levels.get_next_level()
        self.missiles = pygame.sprite.Group()
        player_sprite = Player(self.gameconfig, self.missiles)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.asteroids = pygame.sprite.Group()
        for number in range(level.asteroids_spawning):
            Asteroid(self.asteroids,
                     level,
                     self.gameconfig,
                     self.player.sprite.rect,
                     level.asteroid_default_layers
                     )

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
                    self.score.sprite.add_points(asteroid.get_score())
                    asteroid.handle_hit()
                    missile.kill()

            # Next check if another asteroid hit us
            for asteroid_boink in self.asteroids.sprites():
                if asteroid_boink is not asteroid:
                    if self.check_collision(asteroid, asteroid_boink, False):
                        asteroid.bounce(asteroid_boink)

        if dead:
            self.context.set_state(AsteracoidsStateGameOver(self.gameconfig,
                                                            self.context))
        elif not self.asteroids.sprites():
            self.next_level()

    def updates(self):
        self.score.update()
        self.asteroids.update()
        self.missiles.update()
        self.player.update()
        self.check_collisions()

    def draws(self, screen):
        super().draws(screen)
        self.score.sprite.draw(screen)
        self.asteroids.draw(screen)
        self.missiles.draw(screen)
        self.player.sprite.draw_extended(screen)


class AsteracoidsStateTitle(AsteracoidsState):
    def start_state(self):
        self.title = pygame.sprite.GroupSingle(Title(self.gameconfig))
        title_pos = self.title.sprite.rect.midbottom
        text_pos = (title_pos[0], title_pos[1] + 50)
        press_space = TextRender(self.gameconfig, "Press space to start",
                                 text_pos)
        self.start = pygame.sprite.GroupSingle(press_space)
        self.asteroids = pygame.sprite.Group()
        for number in range(7):
            Asteroid(self.asteroids,
                     LevelThree(),
                     self.gameconfig,
                     pygame.Rect((1, 1), (2, 2)),
                     1
                     )

    def is_go_time(self):
        return self.creation_time + 2000 < pygame.time.get_ticks()

    def updates(self):
        self.asteroids.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.is_go_time():
                self.context.set_state(
                    AsteracoidsStateRunning(self.gameconfig, self.context))

    def draws(self, screen):
        super().draws(screen)
        self.asteroids.draw(screen)
        self.title.draw(screen)
        if self.is_go_time():
            self.start.sprite.draw(screen)


class AsteracoidsStateGameOver(AsteracoidsState):
    def start_state(self):
        center = GameUtils.get_center_pos(self.gameconfig)
        game_over = TextRender(self.gameconfig, "GAME OVER",
                               center)
        self.end = pygame.sprite.GroupSingle(game_over)

    def can_continue(self):
        return self.creation_time + 1000 < pygame.time.get_ticks()

    def updates(self):
        if self.can_continue():
            self.context.set_state(
                AsteracoidsStateTitle(self.gameconfig, self.context))

    def draws(self, screen):
        super().draws(screen)
        self.end.sprite.draw(screen)
