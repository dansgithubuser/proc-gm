from . import utils

import pygame

SUBPIXELS = 8

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_s = 0
        self.y_s = 0
        self.state = None
        path = utils.root_path("assets/tilesets/Toen's Medieval Strategy Sprite Pack v.1.0 (16x16)/Tile-set - Toen's Medieval Strategy (16x16) - v.1.0.png")
        self.image = pygame.image.load(path).subsurface(16, 256, 16, 16).convert_alpha()

    def get_location(self):
        return self.x + self.x_s / SUBPIXELS, self.y + self.y_s / SUBPIXELS

    def get_image(self):
        return self.image

    def handle_action(self, action):
        if not self.state:
            self.state = action

    def update(self):
        d = {
            'n' : ( 0, -1),
            'ne': ( 1, -1),
            'e' : ( 1,  0),
            'se': ( 1,  1),
            's' : ( 0,  1),
            'sw': (-1,  1),
            'w' : (-1,  0),
            'nw': (-1, -1),
        }.get(self.state)
        if d:
            self.x_s += d[0]
            self.y_s += d[1]
            if abs(self.x_s) == SUBPIXELS or abs(self.y_s) == SUBPIXELS:
                self.x += self.x_s // SUBPIXELS
                self.y += self.y_s // SUBPIXELS
                self.x_s = 0
                self.y_s = 0
                self.state = None
