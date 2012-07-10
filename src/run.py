#! /usr/bin/python
import pygame, sys, tiledtmxloader, character, world
from pygame.locals import *
from character import character

# The actual running game
pygame.init()
pygame.display.set_caption("LPC 2012 Python Game")
clock = pygame.time.Clock()

level = world.level1()
screen = pygame.display.set_mode((level.screen_width, level.screen_height))
rect = screen.get_rect()

hero = character("priv/images/character.jpg", rect.center, (level.world_map.pixel_width, level.world_map.pixel_height))
level.sprite_layers[1].add_sprite(hero)


# renderer
renderer = tiledtmxloader.helperspygame.RendererPygame()
# set initial cam position and size
renderer.set_camera_position_and_size(0, 0, level.screen_width, level.screen_height, "topleft")

while 1:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN 
        if event.key == K_RIGHT : hero.xSpeed = down * 3
        elif event.key == K_LEFT : hero.xSpeed = down * -3
        elif event.key == K_UP : hero.ySpeed = down * -3
        elif event.key == K_DOWN : hero.ySpeed = down * 3
        elif event.key == K_ESCAPE : sys.exit(0)
        elif event.key == K_f and down : pygame.display.toggle_fullscreen()
    screen.fill((0, 100, 100))
    # update hero and camera
    hero.update(deltat)
    renderer.set_camera_position(hero.rect.centerx, hero.rect.centery)

    # draw the stuff
    for sprite_layer in level.sprite_layers:
        if sprite_layer.is_object_group:
            # we dont draw the object group layers
            # you should filter them out if not needed
            continue
        else:
            renderer.render_layer(screen, sprite_layer)
    pygame.display.flip()        
