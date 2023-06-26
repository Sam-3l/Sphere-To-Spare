import sys, pygame
from index import index

pygame.init()

window = pygame.display.set_mode((1200, 800), pygame.FULLSCREEN)
pygame.display.set_caption("THE XAG3")
icon = pygame.image.load("icon.png")
icon.set_colorkey((0, 0, 0))
pygame.display.set_icon(icon)

index().run(window)