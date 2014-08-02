#!/usr/bin/python
import pygame

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
BALL_WIDTH, BALL_HEIGHT = 16, 16
BRICK_WIDTH, BRICK_HEIGHT = 64, 16
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 16
PLAYER_SPEED = 10
BALL_SPEED = 2

class Breakout_Sprite(pygame.sprite.Sprite):
    """ Breakout Sprite class that extends following classes

        Attributes:
            image_file (str): Sprite-image filename.
    """
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)

        # load image & rect
        self.image = pygame.image.load('images/' + image_file).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

class Player(Breakout_Sprite):
    """ Bar: Positionned at the bottom of the window,
             but can move horizontally.
    """
    def __init__(self, image_file):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.left = (WINDOW_WIDTH - self.image.get_width()) / 2

	def move_left(self):
		if self.rect.left > 0:
			self.rect.move_ip(-PLAYER_SPEED, 0)

	def move_right(self):
		if self.rect.right < WINDOW_WIDTH:
			self.rect.move_ip(PLAYER_SPEED, 0)

class Brick(Breakout_Sprite):
    """ Brick: Statically positionned in (x, y).
    """
    def __init__(self, image_file, x, y):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.x, self.rect.y = x, y

class Ball(Breakout_Sprite):
    """ Ball: Moves according to speed (speed_x, speed_y).

        Attributes:
            speed_x (int): Ball's x-speed.
            speed_y (int): Ball's y-speed.
    """
    def __init__(self, image_file, speed_x, speed_y):
        Breakout_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT - PLAYER_HEIGHT
        self.rect.left = WINDOW_WIDTH / 2
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        # bounce against borders
        if self.rect.x > WINDOW_WIDTH - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
