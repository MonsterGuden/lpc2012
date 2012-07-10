import pygame, tiledtmxloader

class World():
    def __init__(self, map):
        # load the world
        self.world_map = tiledtmxloader.tmxreader.TileMapParser().parse_decode(map)
        # prepare map rendering
        assert self.world_map.orientation == "orthogonal"
        #prepare loading resources
        self.resources = tiledtmxloader.helperspygame.ResourceLoaderPygame()
        # load images into pygame
        self.resources.load(self.world_map)
        self.screen_width = min(1024, self.world_map.pixel_width)
        self.screen_height = min(768, self.world_map.pixel_height)


class level1(World):
    def __init__(self):
        World.__init__(self, "priv/maps/level1.tmx")
        # retrieve layers
        self.sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(self.resources)

class level2(World):
    def __init__(self):
        World.__init__(self, "priv/maps/level2.tmx")
        # retrieve layers
        self.sprite_layers = tiledtmxloader.helperspygame.get_layers_from_map(self.resources)
