import random

class World:
    def __init__(self, tileset):
        self.w = random.randint(32, 64)
        self.h = random.randint(32, 64)
        self.tileset = tileset
        self.tiles = tileset.generate(self.w, self.h)

    def render(self, screen):
        for layer in self.tiles:
            for y in range(self.h):
                for x in range(self.w):
                    tile = layer[y * self.w + x]
                    if not tile: continue
                    screen.blit(tile, (
                        self.tileset.tile_w * x,
                        self.tileset.tile_h * y,
                    ))
