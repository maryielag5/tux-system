#! /usr/bin/env python

import pygame, sys
from pygame.locals import *

from game import *
from ezmenu import *
from data import *
from cutscenes import *

def RunGame(screen):
    Game(screen)
    play_music("title.mod", 0.75)

def ContinueGame(screen):
    Game(screen, True)
    play_music("title.mod", 0.75)

def Help(screen):
    cutscene(screen, ["AYUDA",
    "",
    "MOVIMIENTO: FECHAS",
    "SALTAR: TECLA Z",
    "RETORNAR: Esc = return",
    ""])

class Menu(object):

    def __init__(self, screen):
        self.screen = screen
        self.menu = EzMenu(["NUEVO JUEGO", lambda: RunGame(screen)], ["CONTINUAR", lambda: ContinueGame(screen)], ["AYUDA", lambda: Help(screen)], ["CERRAR", sys.exit])
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(300, 370)
        self.menu.set_font(pygame.font.Font(filepath("fonts/font.ttf"), 16))
        self.bg = load_image("menu.png")
        self.font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
        self.font2 = pygame.font.Font(filepath("fonts/super-mario-64.ttf"), 45)
        play_music("title.mod", 0.75)
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(40)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                    return

            self.screen.blit(self.bg, (0, 0))
            ren = self.font.render("", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 70))

            ren = self.font2.render("SYSTEM-TUX", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 180))

            ren = self.font2.render("Python", 1, (255, 255, 255))
            self.screen.blit(ren, (320-ren.get_width()/2, 235))



            self.menu.draw(self.screen)
            pygame.display.flip()
