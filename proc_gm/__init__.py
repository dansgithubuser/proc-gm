from . import tileset
from .world import World

import pygame

def run(w=640, h=480, fps=60):
    pygame.init()
    pygame.display.set_caption('Procedural Gamemaster')
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    world = World(tileset.VillageSerene())
    while True:
        player_action = None
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                player_action = {
                    pygame.K_w: 'n',
                    pygame.K_e: 'ne',
                    pygame.K_d: 'e',
                    pygame.K_c: 'se',
                    pygame.K_x: 's',
                    pygame.K_z: 'sw',
                    pygame.K_a: 'w',
                    pygame.K_q: 'nw',
                }.get(event.key)
                continue
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        world.update(player_action)
        screen.fill((0, 0, 0))
        world.render(screen)
        pygame.display.update()
        clock.tick(fps)
