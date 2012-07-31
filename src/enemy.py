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
import tiledtmxloader, pygame, sprite_animation

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

class Enemy(tiledtmxloader.helperspygame.SpriteLayer.Sprite):

    class Waypoints():
        def __init__(self):
            self.waypoints = []
            self.current_waypoint = 0

        def add_waypoint(self, x, y, nr):
            self.waypoints.append((x, y, nr))

        def next_waypoint(self):
            self.current_waypoint += 1
            if(len(self.waypoints) == self.current_waypoint):
               self.current_waypoint = 0

        def get_mission_possition(self, position):
            (waypoint_x, waypoint_y, nr) = self.waypoints[self.current_waypoint]
            (position_x, position_y) = position
            if(position_x == waypoint_x and position_y == waypoint_y):
                self.next_waypoint()
            return self.waypoints[self.current_waypoint]

        def init(self):
            self.waypoints = sorted(self.waypoints, key=lambda waypoint: waypoint[2])


    def __init__(self):
        self.waypoints = self.Waypoints()
        self.speed = 4
        self.direction = UP
        self.view = (0, 0, 0, 0)

    def set_sprite(self, image_location, sprite_width, sprite_height):
        self.image = pygame.image.load(image_location)
        tiledtmxloader.helperspygame.SpriteLayer.Sprite.__init__(self, self.image, self.image.get_rect())
        self.image_width = self.image.get_rect().width
        self.sprite_size = (int(sprite_width), int(sprite_height))
        self.source_rect = pygame.Rect(0, 0, int(sprite_width), int(sprite_height))

    def add_waypoint(self, (x, y, nr)):
        self.waypoints.add_waypoint(x, y, nr)

    def update(self, deltat):
        (waypoint_x, waypoint_y, nr) = self.waypoints.get_mission_possition(self.rect.center)
        (position_x, position_y) = self.rect.center
        if(position_x != waypoint_x):
            if(position_x < waypoint_x):
                position_x += self.speed
                self.direction = RIGHT
            else :
                position_x -= self.speed
                self.direction = LEFT
        if(position_y != waypoint_y):
            if(position_y < waypoint_y):
                position_y += self.speed
                self.direction = DOWN
            else:
                position_y -= self.speed
                self.direction = UP
        self.rect.center = (position_x, position_y)
        self.update_view()
        self.source_rect = self.animation.update(self.direction)

    def update_view(self):
        (x, y, width, height) = self.rect
        center = self.rect.center
        direction = self.direction
        if direction == DOWN:
            self.view = pygame.Rect(x, y, width/2, height)
            self.view.center = center
            self.view.y += height * 0.2
            self.view.height = self.view.height * 3
        elif direction == RIGHT:
            self.view = pygame.Rect(x, y, width, height * 0.7)
            self.view.center = center
            self.view.x += width * 0.2
            self.view.width = width * 3
        elif direction == UP:
            self.view = pygame.Rect(x, y, width/2, height)
            self.view.center = center
            self.view.y -= 2 * height
            self.view.height = height * 3
        elif direction == LEFT:
            self.view = pygame.Rect(x, y, width, height * 0.7)
            self.view.center = center
            self.view.x -= 2 * width + width * 0.2
            self.view.width = width * 3

    def init(self):
        self.waypoints.init()
        (x, y, nr) = self.waypoints.get_mission_possition((0, 0))
        (sprite_width, sprite_height) = self.sprite_size
        self.rect = pygame.Rect(0, 0, sprite_width, sprite_height)
        self.rect.center = (x, y)
        self.animation = sprite_animation.SpriteAnimation(self.image_width, sprite_width, sprite_height)
