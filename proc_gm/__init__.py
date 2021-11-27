import pygame

def run(w=640, h=480, fps=60):
    pygame.init()
    pygame.display.set_caption('Procedural Gamemaster')
    surface = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        surface.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(fps)
