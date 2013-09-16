# -*- coding: utf-8 -*-

#Semone Kallin Clarke
#Mac OSX Mountain Lion
#Python 2.7.2
#Pygame

"""
This is the board class the board object builds the board. When initialized it creates a color list
and a sound list with the colors of the squares and the sounds that should be played on click.

createGrid: creates a grid of the board. This method is used to give an id to the grid positions. The id is later used to
see which sound that should be played.

boardBuild: Builds the initial board. When it is called the flash list is emptied. 

boardPlay: Given the position on the board this function draws a white square here. 

showAll:Draws all the squares. The method is given the position of the flashed square, this is to know which 
sound that should be played.

randRect: Selects a random square on the board and adds it to the flash list. (The flash list contains all the squares that should blink.)

checkClick: Checks if the correct square is clicked by the player. Given the position of the click. The count is used to to get the correct position 
in the flash list. 

All sounds are taken from http://www.soundjay.com/
All images created by me.
"""

import pygame as py
from button import Button
import time
import random

class Board():
    def __init__(self, screen):
        self.startButton = Button("startButton.png", "startButtonHover.png", screen)
        self.screen = screen
        self.index = None
        #Create a colorlist so that the squares get different colors
        self.colorList = [(255, 255, 255), (141, 184, 144), (249, 178, 51), (39,45,112),(153, 47, 47), (129, 163, 208),(242, 114, 28) , (60,109,46),(77,81,76),(114,71,113),(83, 219, 183), (228, 232, 58), (54, 123, 158),(211, 65, 74), (123, 193, 61), (0, 0, 0),(63, 13, 24)]
        self.level = None
        self.grid = None
        self.flash = []
        self.posX = None
        self.posY = None
        #Create a sound list so that the squares gt different sounds
        self.soundList = ["button-1.wav", "button-2.wav","button-3.wav","button-4.wav","button-5.wav", "button-6.wav","button-7.wav","button-8.wav","button-9.wav", "button-10.wav","button-11.wav","button-12.wav","button-13.wav", "button-15.wav","button-15.wav","button-16.wav"]
    
    #Give the grid positions an ID            
    def createGrid(self, level):
        self.grid = []
        ID = 0
        for row in range(level):
            self.grid.append([])
            for column in range(level):
                self.grid[row].append(ID)
                ID += 1
                            
    def boardBuild(self, index):
        self.index = index
        #The level says how many rows and cols there should be
        self.level = index + 2
        #Empty the flash list
        self.flash = []
        
        #Create the grid with id's        
        self.createGrid(self.level)
        
        #Depending on which difficulty the x and y positions are different.
        self.posX = 270 - 50*index - 5*index;
        self.posY = 150 - 50*index - 5*index;
        
        posX = self.posX
        posY = self.posY
    
        ID = 0
        #Draw the squares
        for row in range(self.level):
            for column in range(self.level):
                
                py.draw.rect(self.screen, self.colorList[ID+1], [posX, posY, 100, 100])
                posX += 110
                ID += 1
                        
            posY += 110
            posX -= self.level*110
        
        #Place the start button
        self.startButton.placeButton(325, 570)
    
    def boardPlay(self, pos):   
        #Draw the white square              
        py.draw.rect(self.screen, self.colorList[0], [self.posX + (10+100)*pos[0],self.posY + (10+100)*pos[1], 100, 100])
            
    def showAll(self, pos):        
        posX = self.posX
        posY = self.posY
        ID = 0
        
        c =pos[0]
        r =pos[1]
        #Draw the squares       
        for row in range(self.level):
            for column in range(self.level):
                py.draw.rect(self.screen, self.colorList[ID+1], [posX, posY, 100, 100])
                posX += 110
                ID += 1
                        
            posY += 110
            posX -= self.level*110
        #Play the correct sound
        effect = py.mixer.Sound(self.soundList[self.grid[c][r]])
        effect.play()
    
    #Add a random rectangle to the flash list           
    def randRect(self, level):  
        row = random.randrange(0,level)
        col = random.randrange(0,level)        
        pos = [col, row]
        
        self.flash.append(pos)
    
    def checkClick(self, pos,count):
        #Convert position to column and row for the click.
        column =(pos[0] - self.posX) // (100 + 10)
        row =(pos[1] - self.posY)// (100 + 10 )
        
        #Check if the click column and row matches the flash column and row
        if self.flash[count][0] == column and self.flash[count][1] == row:
            #If match play sound
            effect = py.mixer.Sound(self.soundList[self.grid[column][row]])
            effect.play()
            return 0
        #Check if the player clickes outside the board
        elif column > self.level-1 or row > self.level-1 or column < 0 or row < 0:
            return 1
        else:
            return 2