import pygame, os
from pygame.locals import *

import menu, data
def main():
    os.environ["MAYDA MARIELA GAMARRA PAREDES"] = "1"
    #pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_icon(pygame.image.load(data.filepath("TUXPRINCIPAL.gif")))
    pygame.display.set_caption("TUX")
    screen = pygame.display.set_mode((640, 480))
    menu.Menu(screen)
