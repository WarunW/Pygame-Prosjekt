import pygame as pg

pg.init()

class Ball:
    def __init__(self, vindu, farge:tuple, x_pos:int, y_pos:int, fart_x:int, fart_y:int):
        self._vindu = vindu
        self._farge = farge
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._fart_x = fart_x
        self._fart_y = fart_y
        self._farge = farge

    def tegne(self):
        pg.draw.rect(self._vindu, self._farge, (self._x_pos, self._y_pos, 30, 30))
        pg.display.flip()

    def flytt(self):
        self._x_pos += self._fart_x
        self._y_pos += self._fart_y

        if self._y_pos <= 0 or self._y_pos >= VINDU_HOYDE - 30:
            self._fart_y *= -1

        if self._x_pos <= 0 or self._x_pos >= VINDU_BREDDE - 30:
            self._fart_x *= -1


VINDU_BREDDE = 800
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

vindu.fill((255, 255, 255))
ball = Ball(vindu,(0,0,0),VINDU_BREDDE/2 - 15, VINDU_HOYDE/2 - 15, 0.5, 0.5)

spiller = pg.draw.rect(vindu, (0,0,0), (VINDU_BREDDE - 20, VINDU_HOYDE/2 - 70, 10,140))
motstander = pg.draw.rect(vindu, (0,0,0), (10, VINDU_HOYDE/2 - 70, 10,140))
pg.draw.aaline(vindu, (0,0,0), (VINDU_BREDDE/2,0), (VINDU_BREDDE/2, VINDU_HOYDE))

fortsett = True
while fortsett:
    
    vindu.fill((255, 255, 255))

    spiller = pg.draw.rect(vindu, (0,0,0), (VINDU_BREDDE - 20, VINDU_HOYDE/2 - 70, 10,140))
    motstander = pg.draw.rect(vindu, (0,0,0), (10, VINDU_HOYDE/2 - 70, 10,140))
    pg.draw.aaline(vindu, (0,0,0), (VINDU_BREDDE/2,0), (VINDU_BREDDE/2, VINDU_HOYDE))

    ball.tegne()
    ball.flytt()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    pg.display.flip()

pg.QUIT