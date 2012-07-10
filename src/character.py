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

    def update(self, deltat):
        # move the character
        x, y = self.position
        x += self.xSpeed
        y += self.ySpeed
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # check so we don't walk outside the map
        (mapx, mapy) = self.mapsize
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if mapx < self.rect.right:
            self.rect.right = mapx
        if mapy < self.rect.bottom:
            self.rect.bottom = mapy
