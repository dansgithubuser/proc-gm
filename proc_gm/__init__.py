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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        world.render(screen)
        pygame.display.update()
        clock.tick(fps)
