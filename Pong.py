import pygame as pg

pg.init()

class Ball:
    def __init__(self, vindu, farge:tuple, x_pos:int, y_pos:int, fart_x:float, fart_y:float):
        self._vindu = vindu
        self._farge = farge
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._fart_x = fart_x
        self._fart_y = fart_y
        self._standard = (x_pos, y_pos, fart_x, fart_y) # Lagrer startverdier for restart

    def tegneBall(self):
        pg.draw.rect(self._vindu, self._farge, (self._x_pos, self._y_pos, 30, 30))

    def flyttBall(self):
        self._x_pos += self._fart_x
        self._y_pos += self._fart_y

    def grenserBall(self, spiller, motstander, poengSpiller):
        if self._y_pos <= 0 or self._y_pos >= VINDU_HOYDE - 30:
            self._fart_y *= -1

        if self._fart_x > 0 and self._y_pos + 30 > spiller._y_pos and self._y_pos < spiller._y_pos + 100 and self._x_pos + 30 > spiller._x_pos:
            self._fart_x *= -1
            poengSpiller += 1

        if self._x_pos < motstander._x_pos + 8 and self._y_pos < motstander._y_pos + 100 and self._y_pos + 30 > motstander._y_pos:
            self._fart_x *= -1

        if self._x_pos <= 0 or self._x_pos >= VINDU_BREDDE - 30:
            self.restart()
            self.stopp()

        return poengSpiller

    def stopp(self):
        self._fart_x = 0
        self._fart_y = 0

    def restart(self):
        self._x_pos, self._y_pos, self._fart_x, self._fart_y = self._standard

    def sjekkRestart(self):
        trykkede_taster = pg.key.get_pressed()
        if trykkede_taster[pg.K_SPACE] and self._fart_x == 0 and self._fart_y == 0:
            self.restart()
            return True
        return False

    # Returnerer y-posisjon (brukes av AI)
    def hentY(self):
        return self._y_pos

class Spiller:
    def __init__(self, vindu, farge: tuple, x_pos:int, y_pos:int, fart_y:float):
        self._vindu = vindu
        self._farge = farge
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._fart_y = fart_y
        self._retning = "opp"

    def tegneSpiller(self):
        pg.draw.rect(self._vindu, self._farge, (self._x_pos, self._y_pos, 8,100))

    def flyttSpiller(self, trykkede_taster):
        if self._retning == "opp":
            self._y_pos -= self._fart_y
        elif self._retning == "ned":
            self._y_pos += self._fart_y

    def endreRetningSpiller(self):
        if trykkede_taster[pg.K_UP]:
            self._retning = "opp"
        elif trykkede_taster[pg.K_DOWN]:
            self._retning = "ned"
        
    def grenserSpiller(self):
        if self._y_pos < 0:
            self._y_pos = 0
        if self._y_pos > VINDU_HOYDE - 100:
            self._y_pos = VINDU_HOYDE - 100

    # Enkel AI som følger ballen
    def ai(self, ball_y):
        if self._y_pos + 50 < ball_y:
            self._y_pos += self._fart_y
        elif self._y_pos + 50 > ball_y:
            self._y_pos -= self._fart_y

VINDU_BREDDE = 800
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

vindu.fill((255, 255, 255))
ball = Ball(vindu,(0,0,0),VINDU_BREDDE/2 - 15, VINDU_HOYDE/2 - 15, 0.4, 0.4)
spiller = Spiller(vindu, (0,0,0), VINDU_BREDDE - 20, VINDU_HOYDE/2 - 70, 0.5)
motstander = Spiller(vindu, (0,0,0), 10, VINDU_HOYDE/2 - 70, 0.5)

poengSpiller = 0
font = pg.font.SysFont(None, 50)

pg.draw.aaline(vindu, (0,0,0), (VINDU_BREDDE/2,0), (VINDU_BREDDE/2, VINDU_HOYDE))

fortsett = True
while fortsett:
    
    vindu.fill((255, 255, 255))

    pg.draw.aaline(vindu, (0,0,0), (VINDU_BREDDE/2,0), (VINDU_BREDDE/2, VINDU_HOYDE))

    # Poengtekst
    tekst2 = font.render(str(poengSpiller), True, (0,0,0))
    vindu.blit(tekst2, (VINDU_BREDDE//2 + 40, 20))

    ball.tegneBall()
    if ball.sjekkRestart():
        poengSpiller = 0
    ball.flyttBall()
    poengSpiller = ball.grenserBall(spiller, motstander, poengSpiller)

    # Spiller-input
    trykkede_taster = pg.key.get_pressed()
    spiller.tegneSpiller()
    spiller.flyttSpiller(trykkede_taster)
    spiller.endreRetningSpiller()
    spiller.grenserSpiller()

    # Motstander (AI)
    motstander.ai(ball.hentY())
    motstander.grenserSpiller()
    motstander.tegneSpiller()

    # Avslutte spillet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    pg.display.flip()

pg.QUIT