# LPC 2012 Coding competition entry
# Copyright (C) 2012  Lucas Robsahm
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import pygame, sys, tiledtmxloader, character, world, enemy, util

class Game():
    def __init__(self):
        self.renderer = tiledtmxloader.helperspygame.RendererPygame()
        self.debug = False
        self.fullscreen = False
        self.level = world.World()
        self.first_level()

    def next_level(self):
        if self.level.next_map() == True:
            self.init_map()
            return True
        else:
            return False

    def first_level(self):
        self.level.first_map()
        self.init_map()

    def init_map(self):
        (hero, enemies) = self.level.init_new_map()
        self.level.sprite_layers[1].add_sprite(hero)
        for enemy in enemies:
            self.level.sprite_layers[1].add_sprite(enemy)
            
        self.renderer.set_camera_position_and_size(0, 0, self.level.screen_width, self.level.screen_height, "topleft")

        self.hero = hero
        self.enemies = enemies
    
    def update_camera(self):
        HeroRect = self.hero.rect
        self.renderer.set_camera_position(HeroRect.centerx, HeroRect.centery)
        if self.renderer._cam_rect.top < 0:
            self.renderer._cam_rect.top = 0
            self.renderer.set_camera_rect(self.renderer._cam_rect)
        if self.renderer._cam_rect.left < 0:
            self.renderer._cam_rect.left = 0
            self.renderer.set_camera_rect(self.renderer._cam_rect)
        if self.level.world_map.pixel_width < self.renderer._cam_rect.right:
            self.renderer._cam_rect.right = self.level.world_map.pixel_width
            self.renderer.set_camera_rect(self.renderer._cam_rect)
        if self.level.world_map.pixel_height < self.renderer._cam_rect.bottom:
            self.renderer._cam_rect.bottom = self.level.world_map.pixel_height
            self.renderer.set_camera_rect(self.renderer._cam_rect)


    def update(self, deltat, screen, events):
        for event in events:
            down = event.type == pygame.KEYDOWN
            if event.key == pygame.K_RIGHT : 
                self.hero.xSpeed = down * 6
            elif event.key == pygame.K_LEFT : 
                self.hero.xSpeed = down * -6
            elif event.key == pygame.K_UP : 
                self.hero.ySpeed = down * -6
            elif event.key == pygame.K_DOWN : 
                self.hero.ySpeed = down * 6
            elif event.key == pygame.K_F1 and down : 
                self.debug = not(debug)

        enemies = self.enemies
        hero = self.hero
        # update enemies
        enemies_view = []
        for enemy in enemies:
            enemy.update(deltat)
            enemies_view.append(enemy.view)
            
        # update hero and camera
        hero.update(deltat, self.level.sprite_layers[2])
        self.update_camera()

        # draw the stuff
        for sprite_layer in self.level.sprite_layers:
            if sprite_layer.is_object_group:
                continue
            else:
                self.renderer.render_layer(screen, sprite_layer)

        if self.debug:
            for view in enemies_view:
                pygame.draw.rect(screen, (255, 0, 0), view, 1)
            pygame.draw.rect(screen, (0, 0, 255), hero.rect, 1)

        # haha, or not. you lost!
        if hero.rect.collidelist(enemies_view) != -1:
            return util.STATE_GameOver

        # maybe you did it?
        tiles = util.neighbour_tiles(hero.rect.center,
                                     self.level.sprite_layers[3])
        if(hero.rect.collidelist(tiles) != -1):
            if self.next_level() == False:
                return util.STATE_GameComplete
        return util.STATE_InGame


