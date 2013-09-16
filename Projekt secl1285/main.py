# -*- coding: utf-8 -*-

#Semone Kallin Clarke
#Mac OSX Mountain Lion
#Python 2.7.2
#Pygame

"""
All sounds taken from http://www.soundjay.com/
All images created by me.
"""

import pygame as py
from board import Board
from GUI import GUI

running = True
#Set all screens to false
levelScreen = False
ongoingGame = False
playerTurn = False
gameOver = False
infoScreen = False

#Init the mixer for sound
py.mixer.init(44100, -16, 2, 2048)

#Set up the window
backgroundColor = (232, 232, 232)
screen = py.display.set_mode((1000, 650))
py.display.set_caption("Train Your Brain")
backgroundSurface = py.Surface([1000,650])
backgroundSurface.fill(backgroundColor)
clock = py.time.Clock()

#Set up local variables
fps = 20 
count = 0
index = 0

#Init the board and GUI
board = Board(screen)
gui = GUI(screen,backgroundColor)

#Load images
wait = py.image.load("wait.png")
go = py.image.load("go.png")

#Build the initial screen
gui.initScreenBuild()
initScreen = True

buttonList = [gui.easyButton, gui.mediumButton, gui.hardButton]
py.init()
        
while running:
        for event in py.event.get():
                if event.type == py.QUIT:
                        running = False
                #Check if the mouse is clicked
                if event.type == py.MOUSEBUTTONDOWN and event.button ==1:
                    #Get the position of the click
                    pos = py.mouse.get_pos()
                    #Do if we are at the level screen
                    if levelScreen == True:
                        #Check if home button is clicked
                        if gui.homeButton.clicked(pos):
                            gui.initScreenBuild()
                            initScreen = True
                            levelScreen = False
                            ongoingGame = False
                            playerTurn = False
                        #Check if the start button is clicked
                        if board.startButton.clicked(pos):
                            ongoingGame = True
                            levelScreen = False
                            #Set count to 0
                            count = 0
                    #Do if we are at the info screen
                    if infoScreen == True:
                        #Check if home button is clicked
                        if gui.homeButton.clicked(pos):
                            gui.initScreenBuild()
                            initScreen = True
                            infoScreen = False
                    #Do if we are at the init screen
                    if initScreen == True:
                        if gameOver== True:
                            #Check if home button is clicked (only if game over is true)
                            if gui.homeButton.clicked(pos):
                                gui.initScreenBuild()
                                initScreen = True
                                levelScreen = False
                                ongoingGame = False
                                playerTurn = False
                                gameOver = False
                        #Check if level buttons are clicked                          
                        for lev, button in enumerate(buttonList):
                            if button.clicked(pos):
                                gui.levelScreenBuild(button)
                                board.boardBuild(lev)
                                initScreen = False
                                levelScreen = True
                        #Check if info buttons is clicked                                  
                        if gui.infoButton.clicked(pos):
                             gui.infoScreenBuild()
                             infoScreen = True
                             initScreen = False    
                    #Do if it is the players turn
                    if playerTurn == True:
                        #Check if home button is clicked
                        if gui.homeButton.clicked(pos):
                            gui.initScreenBuild()
                            initScreen = True
                            levelScreen = False
                            ongoingGame = False
                            playerTurn = False
                            gameOver = False
                        #Check if player clicks too many times, (should not be possible)
                        elif count+1 > len(board.flash):
                            print "To Long"
                        #Check if the player clicks the correct square
                        elif board.checkClick(pos, count) == 0:
                            #Add one to count
                            count += 1
                            #Check if the whole flash liste has been clicked
                            if len(board.flash) == count:
                                playerTurn = False
                                #Plays again (adding a flash)
                                ongoingGame = True
                        #Check if click is outside board
                        elif board.checkClick(pos, count) == 1:
                            print "Out of Bounds"
                        else:  
                            #The player has clicked the wrong square... =( send the lengt to know how far player got  
                            gui.gameOverBuild(len(board.flash)-1)
                            playerTurn = False
                            initScreen = True
                            gameOver = True
        #Different screeens, different mouse over checks!                                                                       
        if infoScreen == True:
             gui.homeButton.checkMouseOver()
            
        if initScreen == True:
            for buttons in buttonList:
                buttons.checkMouseOver()
          
            if gameOver == True:
                gui.homeButton.checkMouseOver()
            else:
                gui.infoButton.checkMouseOver()
               
        if levelScreen == True:
            gui.homeButton.checkMouseOver()
            if playerTurn == False and ongoingGame == False:
                board.startButton.checkMouseOver()
        
        #Plays the sequence if ongoing game is true
        if ongoingGame == True:
            #Wait a little so that the player willl be ready
            py.time.wait(250)
            
            count = 0
            #Add to flash list
            board.randRect(board.level)
            
            #Set the loop 
            loop = len(board.flash)*2
            #Get the correct square to flash
            posBoard = board.flash[index]
            
            #Show wait so that the player shoud know to watch and not to click
            screen.blit(wait, (325, 570))
            
            #Play the flash sequence. 
            for i in range(loop):
                #Show white square every second time
                if i%2==0:
                    posBoard = board.flash[index]
                    board.boardPlay(posBoard)
                    index+=1
                #Show all every second time
                else:                    
                    board.showAll(posBoard)    
                #Wait a little so that the player can react.            
                py.time.wait(300)
        
                clock.tick(fps) 
                py.display.update()
            
            ongoingGame = False
            playerTurn = True
            index = 0
        
        #Show go so that the player should know it is its turn    
        if playerTurn == True:
            gui.homeButton.checkMouseOver()
            screen.blit(go, (325, 570))
                
        clock.tick(fps) 
        py.display.update()
              
py.quit()