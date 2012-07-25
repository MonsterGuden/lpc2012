import pygame, tiledtmxloader, sprite_animation

NONE = -1
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

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
        self.direction = UP
        self.mapsize = mapsize
        sprite_width = 64
        sprite_height = 64
        self.image_width = self.image.get_rect().width
        self.source_rect = pygame.Rect(0, 0, sprite_width, sprite_height)
        self.rect = pygame.Rect(0, 0, sprite_width, sprite_height)
        self.rect.center = position
        self.animation = sprite_animation.SpriteAnimation(self.image_width, sprite_width, sprite_height)

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

        # move character if possible, only x or y axis
        if self.xSpeed != 0:
            collision = start_rect.move(self.xSpeed, 0).collidelist(tile_rects)
            if collision != -1:
                if self.xSpeed < 0:
                    self.rect.left = tile_rects[collision].right + 1
                else:
                    self.rect.right = tile_rects[collision].left - 1
            else:
                (old_x, y) = self.rect.center
                new_x = old_x + self.xSpeed
            # set correct direction for animation
                if old_x < new_x: self.direction = RIGHT
                else: self.direction = LEFT
                self.rect.center = (new_x, y)
        elif self.ySpeed != 0:
            collision = start_rect.move(0, self.ySpeed).collidelist(tile_rects)
            if collision != -1:
                if self.ySpeed < 0:
                    self.rect.top = tile_rects[collision].bottom + 1
                else:
                    self.rect.bottom = tile_rects[collision].top - 1
            else:
                (x, old_y) = self.rect.center
                new_y = old_y + self.ySpeed
                if old_y < new_y: self.direction = DOWN
                else: self.direction = UP
                self.rect.center = (x, new_y)
        else:
            self.direction = -1


    def update(self, deltat, collision_tiles):
        # move the character
        self.check_collision_tiles(collision_tiles)
        # check so we don't walk outside the map
        self.check_map_limits()
        self.source_rect = self.animation.update(self.direction)
