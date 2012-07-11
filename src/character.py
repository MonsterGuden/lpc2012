import pygame, tiledtmxloader

# Simple sprite class
class character(tiledtmxloader.helperspygame.SpriteLayer.Sprite):
    def __init__(self, image, position, mapsize):
        self.src_image = pygame.image.load(image)
        tiledtmxloader.helperspygame.SpriteLayer.Sprite.__init__(self, image, self.src_image.get_rect())
        self.image = self.src_image
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_up = self.k_down = 0
        self.xSpeed = self.ySpeed = 0
        self.speed = 3
        self.mapsize = mapsize
        self.rect = self.image.get_rect()
        self.rect.center = position

    def check_map_limits(self):
        (mapx, mapy) = self.mapsize
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if mapx < self.rect.right:
            self.rect.right = mapx
        if mapy < self.rect.bottom:
            self.rect.bottom = mapy

    def check_collision_tiles(self, coll_layer):
        start_rect = self.rect
        (hero_pos_x, hero_pos_y) = self.rect.center
        tile_rects = []
        # find the tile location of our hero
        tile_x = int((hero_pos_x) // coll_layer.tilewidth)
        tile_y = int((hero_pos_y) // coll_layer.tileheight)
        for diry in (-1, 0, 1):
            for dirx in (-1, 0, 1):
                if coll_layer.content2D[tile_y+diry][tile_x+dirx] is not None:
                    tile_rects.append(coll_layer.content2D[tile_y+diry][tile_x+dirx].rect)

        # move character if possible
        collision = start_rect.move(self.xSpeed, 0).collidelist(tile_rects)
        if collision != -1:
            if self.xSpeed < 0:
                self.rect.left = tile_rects[collision].right + 1
            else:
                self.rect.right = tile_rects[collision].left - 1
        else:
            (x, y) = self.rect.center
            x += self.xSpeed
            self.rect.center = (x, y)

        collision = start_rect.move(0, self.ySpeed).collidelist(tile_rects)
        if collision != -1:
            if self.ySpeed < 0:
                self.rect.top = tile_rects[collision].bottom + 1
            else:
                self.rect.bottom = tile_rects[collision].top - 1
        else:
            (x, y) = self.rect.center
            y += self.ySpeed
            self.rect.center = (x, y)


    def update(self, deltat, collision_tiles):
        # move the character
        self.check_collision_tiles(collision_tiles)
        # check so we don't walk outside the map
        self.check_map_limits()
