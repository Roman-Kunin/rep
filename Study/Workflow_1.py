import pygame as pg


WIN_W = 1920
WIN_H = 1080

FPS = 60

pg.init()

pg.display.set_mode((WIN_W, WIN_H))
screen = pg.display.set_caption('Орлог')
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    pg.display.update()
    clock.tick(FPS)
