import pygame, tiledtmxloader, character, enemy, sys
from enemy import Enemy
from character import Character

class World():
    def __init__(self):
        self.next_level = 0
        self.levels = list(["priv/maps/level1.tmx"
                           ,"priv/maps/level2.tmx"])

    def first_map(self):
        self.load_map(self.levels[0])
        self.next_level = 1

    def next_map(self):
        if len(self.levels) == self.next_level:
            self.next_level = -1
            return
        self.load_map(self.levels[self.next_level])
        self.next_level += 1

    def load_map(self, map):
        # load the world
        self.world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode(map)
        # prepare map rendering
        assert self.world_map.orientation == "orthogonal"
        #prepare loading resources
        self.resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
        # load images into pygame
        self.resources.load(self.world_map)
        self.screen_width = 800
        self.screen_height = 600
        self.sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(self.resources)

    def init_new_map(self):
        # temp tables
        objects = []
        enemies_data = []
        enemies = []
        hero = 0

        # get all objects
        for sprite_layer in self.sprite_layers:
            if sprite_layer.is_object_group:
                objects.append(sprite_layer.objects)

        # sort all different variables
        pixel_width = self.world_map.pixel_width
        pixel_height = self.world_map.pixel_height
        for object in objects:
            if object[0].type == "hero":
                position = (int(object[0].x), int(object[0].y))
                sprite_size = (int(object[0].properties['sprite_width']),
                               int(object[0].properties['sprite_height']))
                hero = Character(object[0].properties['sprite'],
                                 position,
                                 sprite_size,
                                 (pixel_width, pixel_height))
            else:
                enemies_data.append(object)

        for enemy_data in enemies_data:
            new_enemy = Enemy()
            for object in enemy_data:
                if object.type == 'enemy':
                    new_enemy.set_sprite(object.properties['sprite'],
                                         object.properties['sprite_width'],
                                         object.properties['sprite_height'])
                elif object.type == 'waypoint':
                    xPosition = int(object.x // self.sprite_layers[0].tilewidth) * self.sprite_layers[0].tilewidth
                    yPosition = int(object.y // self.sprite_layers[0].tileheight) * self.sprite_layers[0].tileheight
                    new_enemy.add_waypoint((xPosition, yPosition, int(object.properties['number'])))
            new_enemy.init()
            enemies.append(new_enemy)

        return (hero, enemies)
