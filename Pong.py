import pygame as pg

pg.init()

VINDU_BREDDE = 800
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

vindu.fill((255, 255, 255))

ball = pg.draw.rect(vindu,(0,0,0),(VINDU_BREDDE/2 - 15, VINDU_HOYDE/2 - 15, 30,30))
spiller = pg.draw.rect(vindu, (0,0,0), (VINDU_BREDDE - 20, VINDU_HOYDE/2 - 70, 10,140))
motstander = pg.draw.rect(vindu, (0,0,0), (10, VINDU_HOYDE/2 - 70, 10,140))
pg.draw.aaline(vindu, (0,0,0), (VINDU_BREDDE/2,0), (VINDU_BREDDE/2, VINDU_HOYDE))

ball_fart_x = 7
ball_fart_y = 7

fortsett = True
while fortsett:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    ball.x += ball_fart_x
    ball.y += ball_fart_y

    pg.display.flip()

pg.QUIT