#! /usr/bin/env python

import pygame
from pygame.locals import *

from data import *
from sprites import *

class Level:

    def __init__(self, lvl=1):
        self.level = pygame.image.load(filepath(("lvl%d.png" % lvl))).convert()
        self.x = 0
        self.y = 0
        for y in range(self.level.get_height()):
            self.y = y
            for x in range(self.level.get_width()):
                self.x = x
                color = self.level.get_at((self.x, self.y))
                if color == (0, 0, 0, 255):
                    l=r=False
                    tile = "middle"
                    if self.get_at(0, -1) != (0, 0, 0, 255):
                        tile = "top"
                    if self.get_at(-1, 0) != (0, 0, 0, 255):
                        l=True
                    if self.get_at(1, 0) != (0, 0, 0, 255):
                        r=True
                    Platform((self.x*32, self.y*32), tile, l, r)

                if color == (0, 19, 127, 255):
                    l=r=False
                    tile = "1"
                    if self.get_at(0, -1) != (0, 19, 127, 255):
                        tile = "middle"
                    if self.get_at(-1, 0) != (0, 19, 127, 255):
                        l=True
                    if self.get_at(1, 0) != (0, 19, 127, 255):
                        r=True

                    Grass((self.x*32, self.y*32), tile, l, r)


                if color == (109, 127, 63, 255):
                    l=r=False
                    tile = "1"
                    if self.get_at(0, -1) != (109, 127, 63, 255):
                        tile = "2"
                    if self.get_at(-1, 0) != (109, 127, 63, 255):
                        l=True
                    if self.get_at(1, 0) != (109, 127, 63, 255):
                        r=True

                    Brick((self.x*32, self.y*32), tile, l, r)

                if color == (48, 48, 48, 255):
                    l=r=False
                    tile = "1"
                    if self.get_at(0, -1) != (48, 48, 48, 255):
                        tile = "2"
                    if self.get_at(-1, 0) != (48, 48, 48, 255):
                        l=True
                    if self.get_at(1, 0) != (48, 48, 48, 255):
                        r=True

                    Gray((self.x*32, self.y*32), tile, l, r)

                if color == (255, 200, 0, 255):
                    AirPlatform((self.x*32, self.y*32))
                if color == (127, 51, 0, 255):
                    PlatformQ((self.x*32, self.y*32))
                if color == (0, 74, 127, 255):
                    Platform_Brick((self.x*32, self.y*32))
                if color == (128, 128, 128, 255):
                    Flag((self.x*31.9, self.y*10))
                if color == (91, 127, 0, 255):
                    Pipe((self.x*32, self.y*28))
                if color == (63, 127, 98, 255):
                    Firebowser((self.x*32, self.y*32))
                if color == (87, 0, 127, 255):
                    Cloud((self.x*32, self.y*32))
                if color == (127, 0, 55, 255):
                    Bush((self.x*32, self.y*27))
                if color == (80, 63, 127, 255):
                    Castle((self.x*32, self.y*22))
                if color == (255, 233, 127, 255):
                    Hill((self.x*32, self.y*27))
                if color == (0, 0, 255, 255):
                    Baddie((self.x*32 + 2, self.y*32 + 4), "monster")
                if color == (0, 255, 255, 255):
                    Baddie((self.x*32 + 1, self.y*32 + 2), "slub")
                if color == (255, 0, 255, 255):
                    Baddie((self.x*32 - 1, self.y*32 - 12), "squidge")
                if color == (76, 255, 0, 255):
                    Cannon((self.x*32 + 1, self.y*29.3 + 4), "cannon") # 1
                if color == (63, 73, 127, 255):
                    Cannon((self.x*32 + 1, self.y*24.5  + 4), "cannonbig") # 1
                if color == (255, 127, 182, 255):
                    Cannon((self.x*32 + 1, self.y*32 + 2), "smallcannon") # 1
                if color == (127, 0, 110, 255):
                    Flower((self.x*32.5, self.y*28.8 + 2), "flower")
                if color == (255, 0, 0, 255):
                    MovingPlatform((self.x*32, self.y*32))
                if color == (82, 127, 63, 255):
                    MovingPlatformtwo((self.x*32, self.y*32))
                if color == (255, 255, 0, 255):
                    Coin((self.x*32 + 4, self.y*32 + 4))
                if color == (0, 255, 0, 255):
                    Bomb((self.x*31.9, self.y*10))
                if color == (0, 200, 0, 255):
                    Spring((self.x*32, self.y*32))
                if color == (200, 0, 0, 255):
                    Boss((self.x*32, self.y*32 + 31))
                if color == (0, 127, 70, 255):
                    MushroomGreen((self.x*31.5, self.y*28))
                if color == (178, 0, 255, 255):
                    PipeBig((self.x*32, self.y*25))
                if color == (64, 64, 64, 255):
                    Fence((self.x*32, self.y*32))
                if color == (182, 255, 0, 255):
                    Tree1((self.x*32, self.y*27))
                if color == (255, 0, 220, 255):
                    Cloud2((self.x*32, self.y*32))
                if color == (72, 0, 255, 255):
                    Rose((self.x*32.23, self.y*27.8 + 2), "flower2")
                if color ==(255, 106, 0, 255):
                    Baddie((self.x*32 + 2, self.y*32 + 4), "monsterred")
                if color ==((38, 127, 0, 255)):
                    Tree2((self.x*32, self.y*29.7))
                if color ==((0, 127, 127, 255)):
                    Grasstexture((self.x*32, self.y*32))
                if color ==((255, 0, 110, 255)):
                    Grass1((self.x*32, self.y*32))
                if color ==((165, 255, 127, 255)):
                    Grass2((self.x*32, self.y*32))
                if color ==((255, 127, 127, 255)):
                    GrassSprite((self.x*32, self.y*32))
                if color ==((127, 255, 197, 255)):
                    Wall((self.x*32, self.y*19))
                if color == ((214, 127, 255, 255)):
                    Castlebig((self.x*32, self.y* 6))
                if color == ((234, 106, 68, 255)):
                    Lava((self.x*32, self.y*32))
                if color == ((127, 89, 63, 255)):
                    Bridge((self.x*32, self.y*32))
                if color == ((127, 116, 63, 255)):
                    Chain((self.x*32, self.y*32))



    def get_at(self, dx, dy):
        try:
            return self.level.get_at((self.x+dx, self.y+dy))
        except:
            pass

    def get_size(self):
        return [self.level.get_size()[0]*32, self.level.get_size()[1]*32]
