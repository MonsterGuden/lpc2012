# simple class to handle sprite animations
# based on lines, will loop the line (x-axis) until line is changed
# (y-axis).
# line is a number (1,2,3) and will be calculated correctly with
# the help of sprite_height.
# if line is -1, the old sprite animation will be returned

import pygame

class SpriteAnimation():
    def __init__(self, image_width, sprite_width, sprite_height):
        self.image_width = image_width
        self.line = 0
        self.rect = pygame.Rect(0, self.line, sprite_width, sprite_height)

    # get the next animation (x-axis) and make sure we dont
    # try to read something outside the image
    def animate(self):
        (animation, line, sprite_width, sprite_height) = self.rect
        if animation + sprite_width == self.image_width:
            new_animation = 0
        else:
            new_animation = animation + sprite_width
        self.rect = pygame.Rect(new_animation, line, sprite_width, sprite_height)
        return self.rect

    # start on a new line (y-axis) with animation 0 (x = 0)
    def new_line(self, line):
        (old_animation, old_line, sprite_width, sprite_height) = self.rect
        self.rect = pygame.Rect(0, line*sprite_height, sprite_width, sprite_height)
        return self.rect

    # check what should be done and do it
    def update(self, line):
        # non-animated when line is -1
        if line == -1:
            return self.rect
        # check if new line or next animation
        if(self.line == line):
            Rect = self.animate()
        else:
            Rect = self.new_line(line)
        self.line = line
        return Rect
