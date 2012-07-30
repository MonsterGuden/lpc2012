#! /usr/bin/python
import pygame, sys, tiledtmxloader, character, world, enemy, util, game
from pygame.locals import *
from character import Character
from world import World
from enemy import Enemy

class Run():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.NewGameScreen = pygame.image.load("priv/images/newgame.png")
        self.GameOverScreen = pygame.image.load("priv/images/gameover.png")
        self.GameCompleteScreen = pygame.image.load("priv/images/gamecomplete.png")
        self.state = util.STATE_NewGame

        # The actual running game
        pygame.init()
        pygame.display.set_caption("LPC 2012 Python Game")
        self.clock = pygame.time.Clock()

    def update(self):
        events = []
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            if event.key == K_ESCAPE and down : sys.exit(0)
            elif event.key == K_f and down : pygame.display.toggle_fullscreen()
            else: events.append(event)

        deltat = self.clock.tick(30)

        if(self.state == util.STATE_NewGame):
            for event in events:
                if event.key == K_n :
                    self.game = game.Game()
                    self.state = util.STATE_InGame
            self.screen.blit(self.NewGameScreen, self.NewGameScreen.get_rect())
        elif(self.state == util.STATE_GameOver):
            for event in events:
                if event.key == K_RETURN : self.state = util.STATE_NewGame
            self.screen.blit(self.GameOverScreen, self.GameOverScreen.get_rect(), None, pygame.BLEND_MAX)
        elif(self.state == util.STATE_GameComplete):
            for event in events:
                if event.key == K_RETURN : self.state = util.STATE_NewGame
            self.screen.blit(self.GameCompleteScreen, self.GameCompleteScreen.get_rect(), None, pygame.BLEND_MAX)
        elif(self.state == util.STATE_InGame):
            self.screen.fill((0, 100, 100))
            self.state = self.game.update(deltat, self.screen, events)

        # draw everything
        pygame.display.flip()

# first time run functionality that start the application
run = Run()
while 1:
    run.update()
