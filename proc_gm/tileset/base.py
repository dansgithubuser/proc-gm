from .. import utils

import pygame

import os

def path(file_name):
    return utils.root_path(f'assets/tilesets/{file_name}')

def spread(center, amount):
    return range(center-amount, center+amount+1)

def march(start, length):
    if length >= 0:
        return range(start, start+length)
    else:
        return range(start+length+1, start+1)

class Tilemap:
    def __init__(self, w, h, tile=None):
        self.w = w
        self.h = h
        self.tiles = [tile] * w * h

    def get(self, x, y):
        if x < 0 or x >= self.w: return None
        if y < 0 or y >= self.h: return None
        return self.tiles[y * self.w + x]

    def set(self, x, y, tile):
        self.tiles[y * self.w + x] = tile

    def subset(self, xi, yi, w, h):
        result = Tilemap(abs(w), abs(h))
        for j, y in enumerate(march(yi, h)):
            for i, x in enumerate(march(xi, w)):
                if x < 0 or x >= self.w: return None
                if y < 0 or y >= self.h: return None
                result.set(i, j, self.get(x, y))
        return result

    def is_all(self, tiles):
        return all(i in tiles for i in self.tiles)

    def has_one(self, tiles):
        return any(i in tiles for i in self.tiles)

    def fill(self, xi, yi, w, h, arg):
        if isinstance(arg, Tilemap):
            for j, y in enumerate(march(yi, h)):
                for i, x in enumerate(march(xi, w)):
                    self.set(x, y, arg.get(i, j))
        else:
            for y in march(yi, h):
                for x in march(xi, w):
                    self.set(x, y, arg)

class Tileset:
    def __init__(self, file_name, tile_w, tile_h):
        image = pygame.image.load(path(file_name)).convert_alpha()
        image_w, image_h = image.get_size()
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.sheet = Tilemap(image_w // tile_w, image_h // tile_h)
        for y, image_y in enumerate(range(0, image_h, tile_h)):
            for x, image_x in enumerate(range(0, image_w, tile_w)):
                self.sheet.set(x, y, image.subsurface((image_x, image_y, tile_w, tile_h)))

    def generate(self, w, h):
        raise Exception('unimplemented')
