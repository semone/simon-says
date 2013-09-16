# -*- coding: utf-8 -*-

#Semone Kallin Clarke
#Mac OSX Mountain Lion
#Python 2.7.2
#Pygame
"""
This is a Button class. Create a button by giving it an image, a hover image and the 
screen. 

placeButton: place the button on the screen by giving the coordintes
checkMouseOver: check if the mouse is over the button and the hover image should be shown
clicked: see if the mouse is over the button and return True
"""
import pygame as py

class Button():
    def __init__(self, image,hoverimage, screen):
        self.screen  = screen
        self.image = py.image.load(image)
        self.name = hoverimage
        self.hoverImage = py.image.load(hoverimage)
        self.x = None
        self.y = None
        
    def placeButton(self, x,y):
        self.x = x
        self.y = y
        self.b = self.screen.blit(self.image, (self.x, self.y))
                        
    def checkMouseOver(self):
        #Check if the mouse is over the image, if so show hover image
        if self.b.collidepoint(py.mouse.get_pos()):
            self.b = self.screen.blit(self.hoverImage, (self.x, self.y))
        else:
            self.b = self.screen.blit(self.image, (self.x, self.y))
            
    def clicked(self, pos):
        #Return true if the button is hovered
        return self.b.collidepoint(pos)
