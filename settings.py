imoprt pygame, sys
from pygame.math import Vector2 as vector


WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 720
TITLE_SIZE = 64
ANIMATION_SPEED = 6

Z_LAYERS = {
    "bg": 0,
    "clouds": 1,
    "bg titles": 2,
    "path": 3,
    "bg details": 4,
    "main": 5,
    "better": 6,
    "fg": 7,
}