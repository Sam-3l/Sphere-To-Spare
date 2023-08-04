import sys, pygame, json
from index import index

pygame.init()

def load():
    with open('settings.json', "r") as file:
        return json.load(file)
    
settings_data = load()
vsync = settings_data["display&graphics"]["vsync"]

if vsync == 0:
    window = pygame.display.set_mode((1600, 900), pygame.HWSURFACE | pygame.DOUBLEBUF, pygame.FULLSCREEN)
else:
    window = pygame.display.set_mode((1200, 800), pygame.FULLSCREEN)

pygame.display.set_caption("SPHERE TO SPARE")
icon = pygame.image.load("icon.png")
icon.set_colorkey((0, 0, 0))
pygame.display.set_icon(icon)

index().run(window)