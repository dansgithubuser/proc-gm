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
        for i in self.entities: i.update(self)

    def render(self, screen):
        screen_w, screen_h = screen.get_size()
        camera_x, camera_y = self.player.get_location()
        for y in range(self.h):
            for x in range(self.w):
                for layer in self.tiles.get(x, y).layers:
                    screen.blit(layer, self.to_view(x, y, camera_x, camera_y, screen_w, screen_h))
        for entity in self.entities:
            x, y = entity.get_location()
            screen.blit(entity.get_image(), self.to_view(x, y, camera_x, camera_y, screen_w, screen_h))

    def to_view(self, x, y, camera_x, camera_y, screen_w, screen_h):
        return (
            int(self.tileset.tile_w * (x - camera_x)) + screen_w // 2 - self.tileset.tile_w // 2,
            int(self.tileset.tile_h * (y - camera_y)) + screen_h // 2 - self.tileset.tile_h // 2,
        )
