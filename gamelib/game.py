#! /usr/bin/env python

import sys, os
import random

import pygame
from pygame.locals import *

from cutscenes import *
from data import *
from sprites import *
from level import *

def RelRect(actor, camera):
    return Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)

class Camera(object):
    def __init__(self, player, width):
        self.player = player
        self.rect = pygame.display.get_surface().get_rect()
        self.world = Rect(0, 0, width, 480)
        self.rect.center = self.player.rect.center

    def update(self):
        if self.player.rect.centerx > self.rect.centerx+64:
            self.rect.centerx = self.player.rect.centerx-64
        if self.player.rect.centerx < self.rect.centerx-64:
            self.rect.centerx = self.player.rect.centerx+64
        if self.player.rect.centery > self.rect.centery+64:
            self.rect.centery = self.player.rect.centery-64
        if self.player.rect.centery < self.rect.centery-64:
            self.rect.centery = self.player.rect.centery+64
        self.rect.clamp_ip(self.world)
    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))

def save_level(lvl):
    open(filepath("saves/prog.sav"), "w").write(str(lvl))

def get_saved_level():
    try:
        return int(open(filepath("saves/prog.sav")).read())
    except:
        open(filepath("saves/prog.sav"),  "w").write(str(1))
        return 1

class Game(object):

    def __init__(self, screen, continuing=False):

        print "sdfsdgsdg"
        self.screen = screen
        self.sprites = pygame.sprite.OrderedUpdates()
        self.players = pygame.sprite.OrderedUpdates()
        self.platforms = pygame.sprite.OrderedUpdates()
        self.grasss = pygame.sprite.OrderedUpdates()
        self.grays = pygame.sprite.OrderedUpdates()
        self.bricks = pygame.sprite.OrderedUpdates()
        self.movingplatforms = pygame.sprite.OrderedUpdates()
        self.movingplatformtwos = pygame.sprite.OrderedUpdates()
        self.baddies = pygame.sprite.OrderedUpdates()
        self.cannons = pygame.sprite.OrderedUpdates()
        self.flowers = pygame.sprite.OrderedUpdates()
        self.firebowsers = pygame.sprite.OrderedUpdates()
        self.roses = pygame.sprite.OrderedUpdates()
        self.nomoveplatforms = pygame.sprite.OrderedUpdates()
        self.coins = pygame.sprite.OrderedUpdates()
        self.explosions = pygame.sprite.OrderedUpdates()
        self.playerdying = pygame.sprite.OrderedUpdates()
        self.bombs = pygame.sprite.OrderedUpdates() # bombs = flagpole
        self.shots = pygame.sprite.OrderedUpdates()
        self.springs = pygame.sprite.OrderedUpdates()
        self.bosses = pygame.sprite.OrderedUpdates()
        self.platformqs = pygame.sprite.OrderedUpdates()
        self.mushroomgreens = pygame.sprite.OrderedUpdates()

        Player.right_images = [load_image("mario1.png"), load_image("mario2.png"), load_image("mario3.png"), load_image("mario4.png"), load_image("mario1.png"), load_image("mario5.png")]
        Platform.images = {"platform-top.png": load_image("platform-top.png"), "platform-middle.png": load_image("platform-top.png")}
        Grass.images = {"grass-1.png": load_image("grass-1.png"), "grass-middle.png": load_image("grass-middle.png")}
        Gray.images = {"gray1.png": load_image("gray1.png"), "gray2.png": load_image("gray2.png")}
        Brick.images = {"brick1.png": load_image("brick1.png"), "brick2.png": load_image("brick2.png")}
        MovingPlatform.image = load_image("moving-platform.png")
        Firebowser.image = load_image("bowser-fireball1.png")
        MovingPlatformtwo.image = load_image("moving-platformlong.png")
        Baddie.left_images1 = [load_image("monster%d.png" % i) for i in range(1, 3)]
        Baddie.left_images2 = [load_image("slub%d.png" % i) for i in range(1, 3)]
        Baddie.left_images3 = [load_image("squidge%d.png" % i) for i in range(1, 3)]
        Baddie.left_images4 = [load_image("monster-red%d.png" % i) for i in range(1, 3)]
        Cannon.left_images1 = [load_image("cannon%d.png" % i) for i in range(1, 3)]
        Cannon.left_images2 = [load_image("cannonbig%d.png" % i) for i in range(1, 3)]
        Cannon.left_images4 = [load_image("smallcannon%d.png" % i) for i in range(1, 3)]
        BaddieBoom.left_images1 = [load_image("monster2.png"), load_image("monster3.png"), load_image("exp1.png"), load_image("exp2.png"), load_image("exp3.png")]
        BaddieBoom.left_images2 = [load_image("slub2.png"), load_image("slub3.png"), load_image("exp1.png"), load_image("exp2.png"), load_image("exp3.png")]
        BaddieBoom.left_images3 = [load_image("squidge2.png"), load_image("squidge3.png"), load_image("exp1.png"), load_image("exp2.png"), load_image("exp3.png")]
        BaddieBoom.left_images4 = [load_image("monster-red2.png"), load_image("monster-red3.png"), load_image("exp1.png"), load_image("exp2.png"), load_image("exp3.png")]
        Coin.images = [load_image("coin%s.png" % i) for i in range(1, 5)]
        CoinDie.images = [load_image("exp2-%d.png" % i) for i in range(1, 4)]
        PlayerDie.right_images = [load_image("mariodie.png"), load_image("exp2-1.png"), load_image("exp2-2.png"), load_image("exp2-3.png")]
        Bomb.image = load_image("flagpole.png")
        Bridge.image = load_image("bridge.png")
        BaddieShot.image = load_image("shot.png")
        CannonShot.image = load_image("cannonbullet1.png")
        CannonShotbig.image = load_image("cannonbullet1.png")
        CannonShotsmall.image = load_image("cannonbullet1.png")
        Spring.images = [load_image("spring1.png"), load_image("spring2.png")]
        AirPlatform.image = load_image("platform-air.png")
        PlatformQ.images = [load_image("platform-q%s.png" % i) for i in range (1, 4)]
        Pipe.image = load_image("pipe.png")
        Flag.image = load_image("flagpole.png")
        Castle.image = load_image("castle.png")
        Castlebig.image = load_image("castle-big.png")
        Hill.image = load_image("hill.PNG")
        Bush.image = load_image("bush-1.png")
        Cloud.image = load_image("cloud.png")
        Cloud2.image = load_image("dobbelclouds.png")
        Platform_Brick.image = load_image("platform-brick.png")
        Boss.left_images = [load_image("bowser1.png"), load_image("bowser2.png"), load_image("bowser3.png")]
        Flower.left_images1 = [load_image("flower%d.png" % i) for i in range(1, 2)]
        MushroomGreen.image = load_image("mushroom-green.png")
        MushroomGreendie.images = [load_image("exp2-%d.png" % i) for i in range(1, 4)]
        PipeBig.image = load_image("pipe-big.png")
        Fence.image = load_image("fence.png")
        Tree1.image = load_image("tree-1.png")
        Tree2.image = load_image("tree-2.png")
        Rose.image = load_image ("rose2.png")
        Grasstexture.image = load_image("grass-texture.png")
        Grass1.image = load_image("grass-1.png")
        Grass2.image = load_image("grass-2.png")
        GrassSprite.image = load_image("grass-texturesprite.png")
        Wall.image = load_image("wall-1.png")
        Lava.image = load_image("lava.png")
        Chain.image = load_image("chain.png")

        Player.groups = self.sprites, self.players
        Platform.groups = self.sprites, self.platforms, self.nomoveplatforms
        Grass.groups = self.sprites, self.grasss, self.nomoveplatforms
        Brick.groups = self.sprites, self.bricks, self.nomoveplatforms
        Gray.groups = self.sprites, self.grays, self.nomoveplatforms
        MovingPlatform.groups = self.sprites, self.platforms, self.movingplatforms
        MovingPlatformtwo.groups = self.sprites, self.platforms, self.movingplatformtwos
        Baddie.groups = self.sprites, self.baddies
        Cannon.groups = self.sprites, self.cannons, self.platforms
        BaddieBoom.groups = self.sprites
        Coin.groups = self.sprites, self.coins
        CoinDie.groups = self.sprites
        MushroomGreen.groups = self.sprites, self.mushroomgreens
        MushroomGreendie.groups = self.sprites
        PlayerDie.groups = self.sprites, self.playerdying
        Bomb.groups = self.sprites, self.bombs
        BaddieShot.groups = self.sprites, self.shots
        CannonShot.groups = self.sprites, self.shots
        CannonShotbig.groups = self.sprites, self.shots
        CannonShotsmall.groups = self.sprites, self.shots
        Spring.groups = self.sprites, self.springs
        AirPlatform.groups = self.sprites, self.platforms, self.nomoveplatforms
        Pipe.groups = self.sprites, self.platforms, self.nomoveplatforms
        PlatformQ.groups = self.sprites, self.platformqs, self.nomoveplatforms, self.platforms
        Platform_Brick.groups = self.sprites, self.platforms, self.nomoveplatforms
        Explosion.groups = self.sprites, self.explosions
        Flag.groups = self.sprites,
        Castle.groups = self.sprites,
        Castlebig.groups = self.sprites,
        Cloud.groups = self.sprites,
        Cloud2.groups = self.sprites,
        Bush.groups = self.sprites,
        Hill.groups = self.sprites,
        Boss.groups = self.sprites, self.bosses
        Flower.groups = self.sprites, self.flowers
        PipeBig.groups = self.sprites, self.platforms, self.nomoveplatforms
        Firebowser.groups = self.sprites, self.firebowsers
        Fence.groups = self.sprites
        Tree1.groups = self.sprites
        Tree2.groups = self.sprites
        Rose.groups = self.sprites, self.roses
        Grasstexture.groups = self.sprites, self.platforms, self.nomoveplatforms
        Grass1.groups = self.sprites, self.platforms, self.nomoveplatforms
        Grass2.groups = self.sprites, self.platforms, self.nomoveplatforms
        GrassSprite.groups = self.sprites
        Wall.groups = self.sprites
        Lava.groups = self.sprites
        Bridge.groups = self.sprites, self.platforms, self.nomoveplatforms
        Chain.groups = self.sprites,

        self.highscore = 0
        self.score = 0
        self.lives = 3
        self.lvl   = 1
        if continuing:
            self.lvl = get_saved_level()
        self.player = Player((0, 0))
        self.clock = pygame.time.Clock()
        self.bg = load_image("background-2.png")
        self.level = Level(self.lvl)
        self.camera = Camera(self.player, self.level.get_size()[0])
        self.font = pygame.font.Font(filepath("fonts/font.ttf"), 16)
        self.heart1 = load_image("mario1.png")
        self.heart2 = load_image("mario-life2.png")
        self.heroimg = load_image("mario5.png")
        self.baddie_sound = load_sound("jump2.wav")
        self.coin_sound = load_sound("coin.wav")
        self.up_sound = load_sound("1up.ogg")
        self.time = 400
        self.running = 1
        self.booming = True
        self.boom_timer = 0
        self.music = "maintheme.mod"
        if self.lvl == 5:
            if continuing:
                self.music = "castle.ogg"
                self.bg = load_image("background-1.png")
        if not continuing:
            cutscene(self.screen,
                     ['NOTA: TUX-SYSTEM',
                      'PRIMERA VERSION',
                      'PRESENTA 4 NIVELES.'])
            stop_music()

        self.intro_level()
        self.main_loop()

    def end(self):
        self.running = 0

    def intro_level(self):
        stop_music()
        self.screen.fill((0, 0, 0))
        self.draw_stats()
        ren = self.font.render("NIVEL %d" % self.lvl, 1, (0, 0, 0))
        self.screen.blit(ren, (320-ren.get_width()/2, 230))
        ren = self.font.render("VIDAS x%d" % self.lives, 1, (0, 0, 0))
        self.screen.blit(ren, (320-ren.get_width()/2, 255))
        pygame.display.flip()
        pygame.time.wait(2500)
        play_music(self.music)

    def next_level(self):
        self.time = 400
        self.booming = True
        self.boom_timer = 0
        try:
            self.lvl += 1
            if self.lvl == 5:
                self.music = "castle.ogg"
            self.clear_sprites()
            self.level = Level(self.lvl)
            self.player = Player((0, 0))
            self.camera = Camera(self.player, self.level.get_size()[0])
            save_level(self.lvl)
            self.intro_level()
        except:
            if self.lives == 0: # Fix =)
                self.lives += 1
            cutscene(self.screen,
            ['LOGRASTE PASAR LOS 4 NIVELES',
             'PRESIONE ENTER PARA CONTINUAR'])


            self.end()

    def redo_level(self):
        self.booming = False
        self.boom_timer = 0
        self.time = 400
        if self.running:
            self.clear_sprites()
            self.level = Level(self.lvl)
            self.player = Player((0, 0))
            self.camera = Camera(self.player, self.level.get_size()[0])
            self.score -= self.score
            self.highscore = self.highscore
            play_music("maintheme.mod")
            #play_music("maintheme.ogg")
            if self.lvl == 5:
                play_music("castle.ogg")

    def show_death(self):
        ren = self.font.render("PERDISTE!!!!!", 2, (50, 200, 70))
        self.screen.blit(ren, (320-ren.get_width()/2, 235))
        pygame.display.flip()
        pygame.time.wait(2500)

    def show_end(self):
        play_music("goal.MOD")
        pygame.time.wait(7500)
        pygame.display.flip()

    def gameover_screen(self):
        stop_music()
        play_music("gameover.mod")
        cutscene(self.screen, ["Game over!!!!"])
        self.end()


    def clear_sprites(self):
        for s in self.sprites:
            pygame.sprite.Sprite.kill(s)

    def main_loop(self):

        while self.running:
            BaddieShot.player = self.player
            CannonShot.player = self.player
            CannonShotbig.player = self.player
            CannonShotsmall.player = self.player
            if not self.running:
                return

            self.boom_timer -= 1

            self.clock.tick(60)
            self.camera.update()
            for s in self.sprites:
                s.update()

            for b in self.bombs:
                if self.player.rect.colliderect(b.rect):
                    self.show_end()
                    self.next_level()
                    self.score += 500
            for s in self.shots:
                if not s.rect.colliderect(self.camera.rect):
                    s.kill()
                if s.rect.colliderect(self.player.rect):
                    self.player.hit()
                    s.kill()
            if self.booming and self.boom_timer <= 0:
                self.redo_level()


            for p in self.platforms:
                p.update()
            self.player.collide(self.springs)
            self.player.collide(self.platforms)

            for g in self.grasss:
                g.update()
            self.player.collide(self.grasss)

            for b in self.bricks:
                b.update()
            self.player.collide(self.bricks)


            for l in self.grays:
                l.update()
            self.player.collide(self.grays)

            for m in self.mushroomgreens:
                if self.player.rect.colliderect(m.rect):
                    m.kill()
                    MushroomGreendie(m.rect.center)
                    self.score += 5000
                    self.lives += 1
                    self.up_sound.play()

            for c in self.coins:
                if self.player.rect.colliderect(c.rect):
                    c.kill()
                    self.coin_sound.play()
                    CoinDie(c.rect.center)
                    self.score += 50

            for p in self.movingplatformtwos:
                p.collide(self.players)
                for p2 in self.platforms:
                    if p != p2:
                        p.collide_with_platforms(p2)

            for p in self.movingplatforms:
                p.collide(self.players)
                for p2 in self.platforms:
                    if p != p2:
                        p.collide_with_platforms(p2)

            for b in self.flowers:
                if self.player.rect.colliderect(b.rect):
                    self.player.hit()

            for f in self.firebowsers:
                if self.player.rect.colliderect(f.rect):
                    self.player.hit()
#________________________________________________________________________

            for b in self.baddies:                               # |
                if b.rect.colliderect(self.camera.rect):         # V
                    if b.type == "squidge":
                        if not random.randrange(70):
                            BaddieShot(b.rect.center)
                if b.type != "squidge":
                    b.collide(self.nomoveplatforms)              # Big problem here somewhere,
                    b.collide(self.springs)                      # The enemies is making the game laggy.
                    b.collide(self.cannons)                      # Main problem would be b.collide(self.nomoveplatforms)
                                                                 # Makes the enemies collide with main platform and for some reason,
                                                                 # that causes alot of problems.
            for c in self.cannons:
                if c.rect.colliderect(self.camera.rect):
                    if c.type == "cannon":
                        if not random.randrange(135):
                            CannonShot(c.rect.center)
                    if c.type != "cannon":
                        c.collide(self.nomoveplatforms)
                        c.collide(self.springs)
                    if c.type == "cannonbig":
                        if not random.randrange(120):
                            CannonShotbig(c.rect.center)
                    if c.type != "cannonbig":
                        c.collide(self.nomoveplatforms)
                        c.collide(self.springs)
                        c.collide(self.cannons)
                    if c.type == "smallcannon":
                         if not random.randrange(145):
                            CannonShotsmall(c.rect.center)
                    if c.type != "smallcannon":
                        c.collide(self.nomoveplatforms)
                        c.collide(self.springs)
                        c.collide(self.cannons)
#_______________________________________________________________________

            for b in self.flowers:
                if self.player.rect.colliderect(b.rect):
                    self.player.hit()

            for r in self.roses:
                if self.player.rect.colliderect(r.rect):
                    self.player.hit()

            for b in self.bosses:
                if self.player.rect.colliderect(b.rect) and not b.dead:
                    self.player.hit()
                if b.die_time <= 0 and b.dead and not self.explosions:
                    pygamesprite.Sprite.kill(b)
                    self.next_level()
                if b.die_time > 0:
                    for s in self.shots:
                        s.kill()
                    if not random.randrange(4):
                        self.boom_sound.play()

            if self.player.rect.right > self.camera.world.w:
                if not self.bombs and self.lvl < 30:
                    self.next_level()
                else:
                    self.player.rect.right = self.camera.world.w

            if self.lvl == 5:
                self.bg = load_image("background-1.png")
                self.music = "castle.ogg"
            else:
                if self.lvl == 6:
                    self.bg = load_image("background-2.png")

            for b in self.baddies:
                if self.player.rect.colliderect(b.rect):
                    if self.player.jump_speed > 0 and \
                       self.player.rect.bottom < b.rect.top+10 and \
                       b.alive():
                        b.kill()
                        self.player.jump_speed = -3
                        self.player.jump_speed = -5
                        self.player.rect.bottom = b.rect.top-1
                        self.score += 100
                        self.baddie_sound.play()
                        BaddieBoom(b.rect.center, b.speed, b.type)
                    else:
                        if b.alive():
                            self.player.hit()

            if self.player.rect.right > self.camera.world.w:
                if not self.bombs and self.lvl < 30:
                    self.next_level()
                else:
                    self.player.rect.right = self.camera.world.w

            if self.player.rect.right > self.camera.world.w:
                self.next_level()

            if self.score > self.highscore:
                self.highscore = self.score

            if self.player.alive():
                self.time -= 0.060
            if self.time <= 0:
                self.player.hit()

            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        self.end()
                    if e.key == K_z:
                        self.player.jump()
            if not self.running:
                return
            self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640, 0))
            self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 + 640, 0))
            self.screen.blit(self.bg, ((-self.camera.rect.x/1)%640 - 640, 0))
            self.camera.draw_sprites(self.screen, self.sprites)
            self.draw_stats()
            for b in self.bosses:
                pygame.draw.rect(self.screen, (255, 0, 0), (170, 64, b.hp*60, 32))
                pygame.draw.rect(self.screen, (0, 0, 0), (170, 64, 300, 32), 1)
            if not self.player.alive() and not self.playerdying:
                if self.lives <= 0:
                    self.gameover_screen()
                else:
                    self.show_death()
                    self.lives -= 1
                    self.redo_level()
            pygame.display.flip()
            if not self.running:
                return

    def draw_stats(self):
        for i in range(1):
            self.screen.blit(self.heart2, (16 + i*34, 16))
        for i in range(self.player.hp):
            self.screen.blit(self.heart1, (16 + i*34, 16))
        self.screen.blit(self.heroimg, (313, 16))
        lives = self.lives
        if lives < 0:
            lives = 0
        ren = self.font.render("Puntaje: %05d" % self.score, 1, (245,20,10))
        self.screen.blit(ren, (624-ren.get_width(),450))
        ren = self.font.render("x%d" % lives, 1, (0,20,100,55))
        self.screen.blit(ren, (315+34, 24))
        ren = self.font.render("NIVEL: %0d" % self.lvl, 1, (200, 0, 100))
        self.screen.blit(ren, (245-ren.get_width(), 16))
        #ren = self.font.render("FPS: %d" % self.clock.get_fps(), 1, (255, 255, 255))
        #self.screen.blit(ren, (511, 41))
        #ren = self.font.render("High:%05d" % self.highscore, 1, (255, 255, 255))
        #self.screen.blit(ren, (260-ren.get_width(), 38))
        ren1 = self.font.render("Tiempo: %d" % self.time, 1, (0,0,0))
        ren2 = self.font.render("Tiempo: %d" % self.time, 1,(0,0,0))
        self.screen.blit(ren1, (30, 450))
        self.screen.blit(ren2, (30, 450))
