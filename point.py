# from typing import Tuple

import pygame
from image import Image


# class represents a movable point


class Point(pygame.sprite.Sprite):
    def __init__(self, pos, img: Image, direction, color):
        '''
        Initialize a Point object

        Args:
            pos (Tuple[int,int]): the coordinate (x,y) of the object
            ing (Image): the image object representing the background
            direction (Tuple(int, int)): the movement direction of the object, as a tuple (dx, dy)
            color (Tuple[int, int, int]): the color f the point, as a tuple (R,G,B)
        '''
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.img = img
        self.direction = direction
        self.check = False

    def update(self):
        '''
        Update the postiotion of the Point object and check for collisions with boudaries

        If a collision occurs with the left, right,top, bottom boundaries, or with a specific
        pixel value in the img image, the object will be removed or marked

        Returns:
            None
        '''
        if self.check:
            return
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]
        if self.direction[0] > 0:
            if self.rect.x >= self.img.pad_w + self.img.width:
                self.kill()
        else:
            if self.rect.x < self.img.pad_w:
                self.kill()
        if self.direction[1] > 0:
            if self.rect.y >= self.img.pad_h + self.img.height:
                self.kill()
        else:
            if self.rect.y < self.img.pad_h:
                self.kill()
        if self.img.img[self.rect.y][self.rect.x] == 255:
            self.check = True
            self.img.img[self.rect.y][self.rect.x] = 0
