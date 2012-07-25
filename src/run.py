#! /usr/bin/python
import pygame, sys, tiledtmxloader, character, world, enemy
from pygame.locals import *
from character import character
from enemy import Enemy

# used to draw debug information
debug = 0

# The actual running game
pygame.init()
pygame.display.set_caption("LPC 2012 Python Game")
clock = pygame.time.Clock()

level = world.level1()
screen = pygame.display.set_mode((level.screen_width, level.screen_height))
rect = screen.get_rect()

hero = character("priv/images/hero.png", rect.center, (level.world_map.pixel_width, level.world_map.pixel_height))
level.sprite_layers[1].add_sprite(hero)

enemies_data = []
enemies = []

# renderer
renderer = tiledtmxloader.helperspygame.RendererPygame()
# set initial cam position and size
renderer.set_camera_position_and_size(0, 0, level.screen_width, level.screen_height, "topleft")

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

for sprite_layer in level.sprite_layers:
    if sprite_layer.is_object_group:
        enemies_data.append(sprite_layer.objects)

for enemy_data in enemies_data:
    new_enemy = Enemy(screen)
    for object in enemy_data:
        if object.type == 'enemy':
            new_enemy.set_sprite(object.properties['sprite'],
                                 object.properties['sprite_width'],
                                 object.properties['sprite_height'])
        elif object.type == 'waypoint':
            xPosition = int(object.x // level.sprite_layers[0].tilewidth) * level.sprite_layers[0].tilewidth
            yPosition = int(object.y // level.sprite_layers[0].tileheight) * level.sprite_layers[0].tileheight
            new_enemy.add_waypoint((xPosition, yPosition, int(object.properties['number'])))
    new_enemy.init()
    enemies.append(new_enemy)
    level.sprite_layers[1].add_sprite(new_enemy)


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
        elif event.key == K_f and down : pygame.display.toggle_fullscreen()
    screen.fill((0, 100, 100))
    # update hero and camera
    hero.update(deltat, level.sprite_layers[2])
    update_camera()

    # update enemies
    enemies_view = []
    for enemy in enemies:
        enemy.update(deltat)
        enemies_view.append(enemy.view)

    # draw the stuff
    for sprite_layer in level.sprite_layers:
        if sprite_layer.is_object_group:
            continue
        else:
            renderer.render_layer(screen, sprite_layer)

    if debug:
        for view in enemies_view:
            pygame.draw.rect(screen, (255, 0, 0), view)
        pygame.draw.rect(screen, (0, 0, 255), hero.rect)

    # draw everything
    pygame.display.flip()

    # haha you lost!
    if hero.rect.collidelist(enemies_view) != -1:
       print("you died!")
       sys.exit(0)
