#! /usr/bin/python
import pygame, sys, tiledtmxloader, character, world, enemy, util
from pygame.locals import *
from character import character
from world import World
from enemy import Enemy

# used to draw debug information
debug = False
fullscreen = False
screen = pygame.display.set_mode((0, 0))

def update_camera():
    HeroRect = hero.rect
    renderer.set_camera_position(HeroRect.centerx, HeroRect.centery)
    if renderer._cam_rect.top < 0:
        renderer._cam_rect.top = 0
        renderer.set_camera_rect(renderer._cam_rect)
    if renderer._cam_rect.left < 0:
        renderer._cam_rect.left = 0
        renderer.set_camera_rect(renderer._cam_rect)
    if level.world_map.pixel_width < renderer._cam_rect.right:
        renderer._cam_rect.right = level.world_map.pixel_width
        renderer.set_camera_rect(renderer._cam_rect)
    if level.world_map.pixel_height < renderer._cam_rect.bottom:
        renderer._cam_rect.bottom = level.world_map.pixel_height
        renderer.set_camera_rect(renderer._cam_rect)

def next_level():
    level.next_map()
    return init_map()

def first_level():
    level.first_map()
    return init_map()

def init_map():
    (hero, enemies) = level.init_new_map()
    level.sprite_layers[1].add_sprite(hero)
    for enemy in enemies:
        level.sprite_layers[1].add_sprite(enemy)

    if(fullscreen):
        screen = pygame.display.set_mode((level.screen_width, level.screen_height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((level.screen_width, level.screen_height))
    renderer.set_camera_position_and_size(0, 0, level.screen_width, level.screen_height, "topleft")

    return (hero, enemies)

# The actual running game
pygame.init()
pygame.display.set_caption("LPC 2012 Python Game")
clock = pygame.time.Clock()

# renderer
renderer = tiledtmxloader.helperspygame.RendererPygame()

level = World()
(hero, enemies) = first_level()

while 1:
    deltat = clock.tick(30)

    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN 
        if event.key == K_RIGHT : hero.xSpeed = down * 6
        elif event.key == K_LEFT : hero.xSpeed = down * -6
        elif event.key == K_UP : hero.ySpeed = down * -6
        elif event.key == K_DOWN : hero.ySpeed = down * 6
        elif event.key == K_ESCAPE : sys.exit(0)
        elif event.key == K_f and down :
            pygame.display.toggle_fullscreen()
            fullscreen = not(fullscreen)
        elif event.key == K_F1 and down : debug = not(debug)
        elif event.key == K_n and down: (hero, enemies) = first_level()
    screen.fill((0, 100, 100))

    # update enemies
    enemies_view = []
    for enemy in enemies:
        enemy.update(deltat)
        enemies_view.append(enemy.view)

    # update hero and camera
    hero.update(deltat, level.sprite_layers[2])
    update_camera()

    # draw the stuff
    for sprite_layer in level.sprite_layers:
        if sprite_layer.is_object_group:
            continue
        else:
            renderer.render_layer(screen, sprite_layer)

    if debug:
        for view in enemies_view:
            pygame.draw.rect(screen, (255, 0, 0), view, 1)
        pygame.draw.rect(screen, (0, 0, 255), hero.rect, 1)

    # draw everything
    pygame.display.flip()

    # maybe you did it?
    tiles = util.neighbour_tiles(hero.rect.center,
                                 level.sprite_layers[3])
    if(hero.rect.collidelist(tiles) != -1):
        (hero, enemies) = next_level()

    # haha, or not. you lost!
    if hero.rect.collidelist(enemies_view) != -1:
       print("you're a bad spy, he saw you!")
       sys.exit(0)
