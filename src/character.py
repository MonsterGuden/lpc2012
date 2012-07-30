import pygame, tiledtmxloader, sprite_animation, util

NONE = -1
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# Simple sprite class
class Character(tiledtmxloader.helperspygame.SpriteLayer.Sprite):
    def __init__(self, image, position, sprite_size, mapsize):
        self.src_image = pygame.image.load(image)
        tiledtmxloader.helperspygame.SpriteLayer.Sprite.__init__(self, image, self.src_image.get_rect())
        self.image = self.src_image
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_up = self.k_down = 0
        self.xSpeed = self.ySpeed = 0
        self.speed = 2
        self.direction = UP
        self.mapsize = mapsize
        (sprite_width, sprite_height) = sprite_size
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
        tile_rects = util.neighbour_tiles(self.rect.center,
                                                coll_layer)
        collision = self.rect.collidelist(tile_rects)
        if(collision != -1):
            tile_rect = tile_rects[collision]
            if(self.direction == DOWN and
               self.rect.bottom > tile_rect.top):
                self.rect.bottom = tile_rect.top - 1
            elif(self.direction == RIGHT and
                 self.rect.right > tile_rect.left):
                self.rect.right = tile_rect.left - 1
            elif(self.direction == LEFT and
                 self.rect.left < tile_rect.right):
                self.rect.left = tile_rect.right + 1
            elif(self.direction == UP and
                 self.rect.top < tile_rect.bottom):
                self.rect.top = tile_rect.bottom + 1

    def move(self):
        if self.xSpeed != 0:
            (old_x, y) = self.rect.center
            new_x = old_x + self.xSpeed
            # set direction
            if old_x < new_x: self.direction = RIGHT
            else: self.direction = LEFT
            self.rect.center = (new_x, y)
        elif self.ySpeed != 0:
            (x, old_y) = self.rect.center
            new_y = old_y + self.ySpeed
            # set correct direction
            if old_y < new_y: self.direction = DOWN
            else: self.direction = UP
            self.rect.center = (x, new_y)
        else:
            # not moving, keep current animation paused
            self.direction = NONE

    def update(self, deltat, collision_tiles):
        # move the character
        self.move()
        #check for tilemap collision
        self.check_collision_tiles(collision_tiles)
        # check so we don't walk outside the map
        self.check_map_limits()
        # animate character
        self.source_rect = self.animation.update(self.direction)
