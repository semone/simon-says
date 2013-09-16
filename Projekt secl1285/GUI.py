# -*- coding: utf-8 -*-

#Semone Kallin Clarke
#Mac OSX Mountain Lion
#Python 2.7.2
#Pygame

"""
This is the GUI class. Different elements are shown depending on where in the game the player is
This class i pretty hardcoded...
The method names are very straight forward.

The sound played on game over was taken from http://www.soundjay.com/ 
"""

import pygame as py
from button import Button

class GUI():
    def __init__(self, screen, backgroundColor):
        self.screen  = screen
        self.backgroundColor =backgroundColor
        self.menu = py.image.load("images/menu.png")

        self.easyButton = Button("images/easyButton.png","images/easyButtonHover.png", self.screen)
        self.mediumButton = Button("images/mediumButton.png","images/mediumButtonHover.png", self.screen)
        self.hardButton = Button("images/hardButton.png", "images/hardButtonHover.png",  self.screen)
        self.homeButton = Button("images/homeButton.png", "images/homeButtonHover.png", self.screen)
        self.infoButton = Button("images/info.png", "images/infoHover.png", self.screen)

    def initScreenBuild(self):
        logo = py.image.load("images/trainLogo.png")
        
        self.screen.fill(self.backgroundColor)
        self.screen.blit(logo,(200,120))
        py.draw.rect(self.screen, (255, 255, 255), py.Rect(750, 0, 250, 650))
        self.screen.blit(self.menu,(812,30))
        self.easyButton.placeButton(823,200)
        self.mediumButton.placeButton(823, 250)
        self.hardButton.placeButton(823, 300)
        self.infoButton.placeButton(823,400)

    def levelScreenBuild(self, button):
        self.screen.fill((self.backgroundColor))
        py.draw.rect(self.screen, (255, 255, 255), py.Rect(750, 0, 250, 650))
        self.screen.blit(self.menu,(812,30))
        levelImage = py.image.load(button.name)
        self.screen.blit(levelImage, (823,200))
        self.homeButton.placeButton(823,570)

    def gameOverBuild(self, count):
        #Play fail sound on build
        py.mixer.music.load('sound/fail_trombone_01.ogg')
        py.mixer.music.play(0)
        
        gameOverIm = py.image.load("images/gameover.png")
        playAgain = py.image.load("images/playagain.png")
        
        #Setup and render score
        scoreFont = py.font.Font("League Gothic.otf", 50)
        score = scoreFont.render("You managed " + str(count) + " rounds\n" , True, (0, 0, 0))
    
        self.screen.fill(self.backgroundColor)
        self.screen.blit(gameOverIm,(200,30))
        self.screen.blit(score, (240, 500))
        py.draw.rect(self.screen, (255, 255, 255), py.Rect(750, 0, 250, 650))
        self.screen.blit(playAgain,(812,100))
        self.easyButton.placeButton(823,200)
        self.mediumButton.placeButton(823, 250)
        self.hardButton.placeButton(823, 300)
        self.homeButton.placeButton(823,570)

    def infoScreenBuild(self):
        fontHeadLine = py.font.Font("League Gothic.otf", 36)
        headLine = fontHeadLine.render("This is how you play the game:", True, (0, 0, 0))

        fontText = py.font.SysFont("monospacems", 26)

        text1 = fontText.render("Do as the computer. Watch the sequence the computer plays and then repeat", True, (0, 0, 0))
        text2 = fontText.render("the same sequence, easy huh? When the computer plays you will see a wait ", True, (0, 0, 0))
        text3 = fontText.render("sign,a go! sign will be shown when its your turn. There are three different ", True, (0, 0, 0))
        text4 = fontText.render("levels to be played, Easy, Medium and Hard. The different levels have", True, (0, 0, 0))
        text5 = fontText.render("different amount of squares that can blink.", True, (0, 0, 0))
        text6 = fontText.render("No high score function is implemented yet, so for now you can just train your brain!", True, (0, 0, 0))
        
        py.draw.rect(self.screen, self.backgroundColor, py.Rect(0, 0, 750, 650))
        py.draw.rect(self.screen, (255, 255, 255), py.Rect(750, 0, 250, 650))
        self.screen.blit(self.menu,(812,30))
        self.screen.blit(headLine, (60, 150))
        self.screen.blit(text1, (60, 250))
        self.screen.blit(text2, (60, 275))
        self.screen.blit(text3, (60, 300))
        self.screen.blit(text4, (60, 325))
        self.screen.blit(text5, (60, 350))
        self.screen.blit(text6, (60, 400))
    
        self.homeButton.placeButton(823,570)