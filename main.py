#NOTE: this project obviously doesnt belong to me and I simply am using the asset that is provided by the youtuber.
#orig project: https://github.com/clear-code-projects/UltimatePygameIntro/tree/main

import pygame as pg 
from sys import exit
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#important because for some reason it runs in another folder on my machine

pg.init()

screen = pg.display.set_mode((800, 400))
pg.display.set_caption("game title") #title set on top of the window
clock = pg.time.Clock() #variable to set max framerate later on
font = pg.font.Font('font/Pixeltype.ttf',50)


sky_s = pg.image.load('graphics/Sky.png').convert() #convert make game faster prtty much
ground_s = pg.image.load('graphics/ground.png').convert()
txt_s = font.render("snail game", False, 'Black').convert()


snail_s = pg.image.load("graphics/snail/snail1.png").convert_alpha() #IF THE BACKGROUND IS TRANSPARENT
snail_rect = snail_s.get_rect(midbottom = (600, 300))

player_s = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_s.get_rect(midbottom = (80, 300))

while True: #to run forever
    for event in pg.event.get(): #check events detected by the game
        if event.type == pg.QUIT:
            pg.quit()
            exit() #prtty much make it quit
        #if event.type == pg.MOUSEMOTION:
        #    if player_rect.colliderect(event.pos): print("collision")




    screen.blit(sky_s,(0, 0)) #put the surface on the screen
    screen.blit(ground_s,(0, 300))
    screen.blit(txt_s, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_s, snail_rect)
    screen.blit(player_s, player_rect)
    """
    if player_rect.colliderect(snail_rect): #works because python assume you check if its true by default
       print("collision")

    mouse_pos = pg.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        pg.mouse.get_pressed()     (to check which mouse button gets pressed)
    """
    pg.display.update() #make the game update in a infinite loop
    clock.tick(60) #set max framerate to 60 fps