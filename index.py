import pygame, sys
from mainmenu import loading, mainmenu

pygame.init()

class index:
    def __init__(self):
        self.image = pygame.image.load("logo.png")
        self.clock = pygame.time.Clock()

    def run(self, window):
        self.width, self.height = window.get_size()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        running = True
        opacity = 0
        points = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

            window.fill((0, 0, 0))
            
            if points >= 255:
                opacity -= 3
                if opacity <= 0:
                    loading().run(window)
                    return "done"
            else:
                opacity += 3
                points += 3

            self.image.set_alpha(opacity)
            window.blit(self.image, (0, 0))

            pygame.display.flip()
            self.clock.tick(40)
