import pygame as game


game.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = game.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

game.display.set_caption('Battle')
img = game.image.load('images/')

run = True
while run:
    for event in game.event.get():
        #quit game
        if event.type == game.QUIT:
            run = False


