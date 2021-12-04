from . import player

import random

class World:
    def __init__(self, tileset):
        self.w = random.randint(32, 64)
        self.h = random.randint(32, 64)
        self.tileset = tileset
        self.tiles = tileset.generate(self.w, self.h)
        self.player = player.Player(0, self.h // 2)
        self.entities = [self.player]

    def update(self, player_action):
        self.player.handle_action(player_action)
        for i in self.entities: i.update()

    def render(self, screen):
        x_camera, y_camera = self.player.get_location()
        for layer in self.tiles:
            for y in range(self.h):
                for x in range(self.w):
                    tile = layer[y * self.w + x]
                    if not tile: continue
                    screen.blit(tile, (
                        int(self.tileset.tile_w * (x - x_camera)),
                        int(self.tileset.tile_h * (y - y_camera)),
                    ))
        for entity in self.entities:
            x, y = entity.get_location()
            screen.blit(entity.get_image(), (
                int(self.tileset.tile_w * (x - x_camera)),
                int(self.tileset.tile_h * (y - y_camera)),
            ))
