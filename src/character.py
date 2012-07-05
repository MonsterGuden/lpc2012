import pygame

# Simple sprite class
class character(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.image = self.src_image
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_up = self.k_down = 0
        self.xSpeed = self.ySpeed = 0

    def update(self, deltat):
        x, y = self.position
        x += self.xSpeed
        y += self.ySpeed
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
