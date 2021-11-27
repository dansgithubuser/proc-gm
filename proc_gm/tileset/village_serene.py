from .base import spread, march, Tilemap, Tileset

from .. import utils

import math
import random

class VillageSerene(Tileset):
    def __init__(self):
        Tileset.__init__(self, 'Serene_Village_16x16.png', 16, 16)

    def generate(self, w, h):
        self.grass = self.sheet.get(3, 0)
        self.road = self.sheet.get(10, 2)
        self.houses = [
            self.sheet.subset( 0, 21, 3, 4),
            self.sheet.subset( 3, 21, 3, 4),
            self.sheet.subset( 6, 21, 4, 4),
            self.sheet.subset(10, 21, 5, 4),
            self.sheet.subset( 0, 25, 5, 4),
            self.sheet.subset( 5, 25, 5, 4),
            self.sheet.subset(10, 25, 3, 4),
            self.sheet.subset(13, 25, 3, 4),
        ]
        while True:
            ground = Tilemap(w, h, self.grass)
            doodads = Tilemap(w, h)
            self._generate_roads(ground, doodads, w, h)
            self._generate_houses(ground, doodads, w, h)
            if self.n_houses > 3: break
        self._finalize_roads(ground, doodads, w, h)
        self._generate_trees(ground, doodads, w, h)
        self._generate_rocks(ground, doodads, w, h)
        self._generate_flowers(ground, doodads, w, h)
        return [ground.tiles, doodads.tiles]

    def _generate_roads(self, ground, doodads, w, h):
        main_road_y = random.randint(h * 2 // 5, h * 3 // 5)
        # main road
        for y in spread(main_road_y, 1):
            for x in range(0, w):
                ground.set(x, y, self.road)
        # secondary roads
        roadiness = random.uniform(0.1, 0.2)
        road_length = lambda x: random.randint(0, int(h / 3 * math.sin(x/w * math.pi))) + 5
        skip = 0
        for x in range(0, w):
            if skip:
                skip -= 1
                continue
            if random.random() < roadiness:
                r = random.random()
                u = r < 0.75
                d = r < 0.5 or r > 0.75
                if u:
                    l = road_length(x)
                    for y in march(main_road_y, -l):
                        for i in range(2):
                            ground.set(x+i, y, self.road)
                if d:
                    l = road_length(x)
                    for y in march(main_road_y, +l):
                        for i in range(2):
                            ground.set(x+i, y, self.road)
                skip = int(1 / roadiness)

    def _generate_houses(self, ground, doodads, w, h):
        self.n_houses = 0
        housiness = random.uniform(0.5, 0.75)
        for y in utils.rand_range(h):
            for x in utils.rand_range(w):
                if random.random() > housiness: continue
                house = random.choice(self.houses)
                foundation_rect = (x, y-1, house.w, -house.h)
                foundation = ground.subset(*foundation_rect)
                if not foundation: continue
                if not foundation.is_all([self.grass]): continue
                if not doodads.subset(*foundation_rect).is_all([None]): continue
                driveway_rect = (x, y, house.w, 2)
                driveway = ground.subset(*driveway_rect)
                if not driveway: continue
                if not driveway.is_all([self.grass]): continue
                road_l = ground.subset(x-1, y, 1, 2)
                road_r = ground.subset(x+house.w, y, 1, 2)
                if not road_l: continue
                if not road_r: continue
                if not any([
                    road_l.is_all([self.road]),
                    road_r.is_all([self.road]),
                ]): continue
                space = ground.subset(x, y+2, house.w, 2)
                if not space.is_all([self.grass]): continue
                doodads.fill(*foundation_rect, house)
                ground.fill(*driveway_rect, self.road)
                self.n_houses += 1

    def _finalize_roads(self, ground, doodads, w, h):
        def neighbors(x, y):
            result = []
            if ground.get(x, y-1) != self.grass: result.append('N')
            if ground.get(x+1, y) != self.grass: result.append('E')
            if ground.get(x, y+1) != self.grass: result.append('S')
            if ground.get(x-1, y) != self.grass: result.append('W')
            if len(result) == 4:
                result = []
                if ground.get(x+1, y-1) == self.grass: result.append('ne')
                if ground.get(x+1, y+1) == self.grass: result.append('se')
                if ground.get(x-1, y+1) == self.grass: result.append('sw')
                if ground.get(x-1, y-1) == self.grass: result.append('nw')
            return ''.join(result)

        edges = {
            'NE': lambda: self.sheet.get(5, 1),
            'ES': lambda: self.sheet.get(5, 2),
            'SW': lambda: self.sheet.get(3, 2),
            'NW': lambda: self.sheet.get(3, 1),
            'NES': lambda: self.sheet.get(5, 3),
            'ESW': lambda: self.sheet.get(random.randint(7, 8), 3),
            'NSW': lambda: self.sheet.get(3, 3),
            'NEW': lambda: self.sheet.get(random.randint(7, 8), 1),
            'ne': lambda: self.sheet.get(6, 3),
            'se': lambda: self.sheet.get(6, 1),
            'sw': lambda: self.sheet.get(9, 1),
            'nw': lambda: self.sheet.get(9, 3),
        }
        for y in range(h):
            for x in range(w):
                if ground.get(x, y) != self.road: continue
                tile = edges.get(neighbors(x, y))
                if tile: ground.set(x, y, tile())

    def _generate_trees(self, ground, doodads, w, h):
        pass

    def _generate_rocks(self, ground, doodads, w, h):
        pass

    def _generate_flowers(self, ground, doodads, w, h):
        pass
