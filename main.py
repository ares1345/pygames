import pygame as pg 
from sys import exit
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#important because for some reason it runs in another folder on my machine

pg.init()

screen = pg.display.set_mode((800, 400))
pg.display.set_caption("god this is gonna be bad") #title set on top of the window
clock = pg.time.Clock() #variable to set max framerate later on
font = pg.font.Font('font/Pixeltype.ttf',50)


sky_s = pg.image.load('graphics/Sky.png').convert() #convert make game faster prtty much
ground_s = pg.image.load('graphics/ground.png').convert()
txt_s = font.render("I WANNA KILL MYSELF", False, 'Black').convert()


snail_s = pg.image.load("graphics/snail/snail1.png").convert_alpha() #IF THE BACKGROUND IS TRANSPARENT
snail_x_pos = 600

player_s = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_s.get_rect(midbottom = (80, 300))

while True: #to run forever
    for event in pg.event.get(): #check events detected by the game
        if event.type == pg.QUIT:
            pg.quit()
            exit() #prtty much make it quit



    screen.blit(sky_s,(0, 0)) #put the surface on the screen
    screen.blit(ground_s,(0, 300))
    screen.blit(txt_s, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos <= -150: snail_x_pos = 800
    screen.blit(snail_s, (snail_x_pos, 268))
    screen.blit(player_s, player_rect)




    pg.display.update() #make the game update in a infinite loop
    clock.tick(60) #set max framerate to 60 fps



