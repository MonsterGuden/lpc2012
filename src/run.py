#! /usr/bin/python
import pygame, sys, tiledtmxloader, character, world
from pygame.locals import *
from character import character

# The actual running game
pygame.init()
clock = pygame.time.Clock()

level = world.level1()
screen = pygame.display.set_mode((level.screen_width, level.screen_height))
rect = screen.get_rect()

picture = character("priv/images/character.jpg", rect.center)
picture_group = pygame.sprite.RenderPlain(picture)

# renderer
renderer = tiledtmxloader.helperspygame.RendererPygame()
# set initial cam position and size
renderer.set_camera_position_and_size(level.cam_world_pos_x, level.cam_world_pos_y, level.screen_width, level.screen_height, "topleft")


while 1:
    deltat = clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN 
        if event.key == K_RIGHT : picture.xSpeed =  down
        elif event.key == K_LEFT : picture.xSpeed = -down
        elif event.key == K_UP : picture.ySpeed = -down
        elif event.key == K_DOWN : picture.ySpeed = down
        elif event.key == K_ESCAPE : sys.exit(0)
        elif event.key == K_f and down : pygame.display.toggle_fullscreen()
    screen.fill((0, 0, 0))
    for sprite_layer in level.sprite_layers:
        if sprite_layer.is_object_group:
            # we dont draw the object group layers
            # you should filter them out if not needed
            continue
        else:
            renderer.render_layer(screen, sprite_layer)
    picture_group.update(deltat)
    picture_group.draw(screen)

    pygame.display.flip()
