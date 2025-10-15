# experiemntal class im working on

import pygame
import sys
import objects.image
class environment(objects.image.still,pygame.sprite.Sprite):
    def __init__(self, Start_x, Start_y,width,height,wallColor=None,image_to_use=None,load_path=None): # possiblity to use images as environment but not neccessary
        super().__init__(x, y,width,height,image_to_use)
        self.x = Start_x
        self.y = Start_y
        self.width = width
        self.height = height
        self.wallColor = wallColor
        self.load_path = load_path

    def wall_classic(self):
        try:
            startX = self.x
            startY = self.y
            self.image = pygame.Surface([self.width, self.height],pygame.SRCALPHA).convert_alpha()
            pygame.draw.rect(self.image,(self.wallColor),(0,0,self.width,self.height))
            self.rect = self.image.get_rect(topleft =(startX,startY))
            self.mask  = pygame.mask.from_surface(self.image)
        except:
            print("ERROR: make sure you hvae entered the starting x adn y values, width and height and the wall Color")
        img_load = pygame.image.load(self.load_path) 
        self.image = pygame.transform.scale(img_load , (self.width, self.height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))