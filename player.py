from pickle import FALSE
import pygame as py
import colors, constants, sys

class player:
    def __init__(self, x, y) -> None:
        # x and y are distances w.r.t (0,0)
        self.x = x
        self.y = y
        self.width = constants.PLATFORM_WIDTH
        self.height = constants.PLAYER_HEIGHT
        self.surface = py.Surface(constants.PLAYER_SIZE)
        self.moving_left = False
        self.moving_right = False
        self.moving_down = True
        self.jump = False
        self.jump_momemntum = -20.0
        self.momentum = 0.0
        self.prev_momentum = 0.0

    def draw(self, screen):
        self.surface.fill(colors.BLACK)
        screen.blit(self.surface, (self.x, self.y))

    def get_input(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_d:
                    self.moving_right = True

                if event.key == py.K_a:
                    self.moving_left = True

                if event.key == py.K_w and self.jump == False:
                    self.jump = True
                    self.momentum = self.jump_momemntum

            elif event.type == py.KEYUP:
                if event.key == py.K_d:
                    self.moving_right = False

                if event.key == py.K_a:
                    self.moving_left = False
            #self.move()

    def move(self, platforms, offset):
        scroll = 0.0
        if self.moving_left:
            scroll -= constants.PLAYER_SPEED
            offset -= scroll

        if self.moving_right:
            scroll += constants.PLAYER_SPEED
            offset -= scroll

        offset = self.check_collisions(platforms, offset, "horizontal", scroll)

        self.y += self.momentum
        self.prev_momentum = self.momentum
        self.momentum += constants.GRAVITY

        offset = self.check_collisions(platforms, offset, "vertical", scroll)
        return scroll, offset

    def check_collisions(self, platforms, offset, direction, scroll):
        bansal_rect = self.surface.get_rect()
        bansal_rect.center = (self.x + constants.PLAYER_WIDTH/2.0, self.y + constants.PLAYER_HEIGHT/2.0)
        for platform in platforms:
            platform_rect = platform.surface.get_rect()
            platform_rect.center = (platform.x + offset + platform.width/2.0, platform.y + platform.height/2.0)
            if bansal_rect.colliderect(platform_rect):
                if direction == "horizontal":
                    if self.moving_right or self.moving_left:
                        offset += scroll
                else:
                    if self.prev_momentum >= 0.0:
                        self.y = platform.y - constants.PLAYER_HEIGHT
                        self.jump = False
                    else:   
                        pass
                    self.momentum, self.prev_momentum = 0.0, 0.0

        return offset