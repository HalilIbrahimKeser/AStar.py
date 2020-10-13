"""
Karaktersatt Obligatorisk Oppgave #1

Brukte denne hjemmesiden til å implementere kode: https://www.kalmanfilter.net/alphabeta.html
"Example 2 – Tracking the constant velocity aircraft in one dimension"

Samme som i vårt eksempel er hastigheten konstant, den endrer seg ikke over tid. Det fremkommer en lineær funskjon.
Y= aX + b

Jeg bruker et alpa beta filter til oppgaven.

I denne sammenheng har vi ikke en "track-to-track interval is Δt" så jeg prøver ut forskjellige verdier og prøver ut.
Samme gjelder verdiene til alpha og beta.

Mine beregnede self._xn_n_minus_1 som en predikert verdi,
treffer ganske godt med rectangelets virkelige posisjon som er self.rect.x.
Eksempel fra print fra consolen under:
self.rect.x: 		 998
self._xn_n_plus_1:  947.8297573858339

Prøvde å få litt hjelp fra nettmøtene, men det var ingen hjelp å få. 13.10.20.
Prøvde både på dagmøtet og kveldsmøtet.

Halil Ibrahim Keser
"""

import pygame as pg
from random import random, randint
import numpy as np
from numpy.linalg import norm

fps = 0.0


class Projectile():

    def __init__(self, background, kalman=None):
        self.background = background
        self.rect = pg.Rect((800, 700), (16, 16))
        self.px = self.rect.x
        self.py = self.rect.y
        self.dx = 0.0
        self.kalm = kalman

    def move(self, goal):
        if self.kalm:
            goal = self.kalm.calc_next(goal)

        deltax = np.array(float(goal) - self.px)  # The track-to-track interval is Δt or Δx ?
        # print("deltax: \t\t\t", deltax)
        mag_delta = norm(deltax)  # * 500.0   # magnitude
        np.divide(deltax, mag_delta, deltax)

        self.dx += deltax
        # if self.dx:
        # self.dx /= norm(self.dx) * 50

        self.px += self.dx / 50.0
        self.py += -0.5
        try:
            self.rect.x = int(self.px)
        except:
            pass
        try:
            self.rect.y = int(self.py)
        except:
            pass


class Target():
    def __init__(self, background, width):
        self.background = background
        self.rect = pg.Rect(self.background.get_width() // 2 - width // 2,
                            50, width, 32)
        self.dx = 1 if random() > 0.5 else -1

    def move(self):
        self.rect.x += self.dx

        if self.rect.x < 300 or self.rect.x > self.background.get_width() - 300:
            self.dx *= -1
        # print("\nself.rect.x: \t\t", self.rect.x)

    def noisy_x_pos(self):
        pos = self.rect.x
        center = self.rect.width // 2
        noise = np.random.normal(0, 1, 1)[0]
        return pos + center + noise * 300.0


class Kalman():
    def __init__(self):
        """Initialization"""
        self._n = 0.0                # Iterasjons verdi
        self._z_n = 0.0              # Inkommende måling av range (avstand av nois som fremkommer) fra radar
        self._xn_n = 0.0             # Avstand i tid n=n. Jeg predikerer et tall
        self._xn_n_minus_1 = 0.0     # Avstand i tid n=n-1
        self._xn_n_plus_1 = 0.0      # Avstand i tid n=n+1
        """Kalman Gain"""            # Kalman gain i dette sammenheng er apha og beta
        self._Kn = 0.1
        self._alpha = 0.1               # alpha filter
        self._beta = 0.2              # beta filter
        self._delta_t = 300           # The track-to-track interval Δt. 1/clock.get_fps()
        """Velocity"""
        self._xdotn_n = 0.0             # Velocity/hastighet i tid n=n
        self._xdotn_n_minus_1 = 0.0     # Velocity/hastighet i tid n=n-1
        self._xdotn_n_plus_1 = 0.0      # Velocity/hastighet i tid n=n+1
        """Measurement uncertainty"""
        self._r = 0.0
        self._Pn_n = 0.0                # Measurement uncertainty i tid n=n
        self._Pn_n_minus_1 = 0.0        # Measurement uncertainty i tid n=n-1
        self._Pn_n_plus_1 = 0.0         # Measurement uncertainty i tid n=n+1

    """The Update State Equation for position"""
    def StateUpdateEquationPosition(self):
        stateUpdateEquationDataPosition = self._xn_n_minus_1 + self._alpha * (self._z_n - self._xn_n_minus_1)
        return stateUpdateEquationDataPosition

    """The Update State Equation for velocity"""
    def StateUpdateEquationVelocity(self):
        stateUpdateEquationDataVelocity = \
            self._xdotn_n_minus_1 + (self._beta * ((self._z_n - self._xn_n_minus_1) / self._delta_t))
        return stateUpdateEquationDataVelocity

    """The Update State Equation for velocity"""
    def StateExtrapolationEquation(self):
        self._xn_n_plus_1 = self._xn_n + (self._delta_t * self._xdotn_n)
        self._xdotn_n_plus_1 = self._xdotn_n
        stateExtrapolationEquation = self._xn_n_plus_1
        return stateExtrapolationEquation

    """Measurement uncertainty, Kalman Gain"""
    def MeasurementUncertainty(self):
        self._Pn_n = (1 - self._alpha) * self._Pn_n_minus_1
        self._r = self._z_n - self._xn_n
        self._alpha = self._Pn_n_minus_1 / (self._Pn_n_minus_1 + self._r)

        measurementUncertainty = self._Pn_n + ((self._delta_t * self._delta_t) * self._Pn_n)
        return measurementUncertainty

    """The Main. Hovedfunksjon"""
    def calc_next(self, z_i):
        """Step 1: MEASURE, z_n fa innkommende verdi"""
        self._z_n = z_i

        """Step 2: UPDATE, State Update, estimerer current state"""
        self._xn_n = self.StateUpdateEquationPosition()
        self._xdotn_n = self.StateUpdateEquationVelocity()

        """Step 3: Prediction"""
        self._xn_n_plus_1 = self.StateExtrapolationEquation()

        """Iteration"""
        self._n += 1
        self._xn_n_minus_1 = self._xn_n
        self._xdotn_n_minus_1 = self._xdotn_n


        # print("self._xn_n: ", self._xn_n)
        # print("self._xn_n_plus_1: ", self._xn_n_plus_1)
        # print("self._z_n: ", self._z_n)
        # print("self._xdotn_n: ", self._xdotn_n)

        return self._xn_n


pg.init()
w, h = 1600, 800
background = pg.display.set_mode((w, h))
surf = pg.surfarray.pixels3d(background)
running = True
clock = pg.time.Clock()

kalman_score = 0
reg_score = 0
iters = 0

while running:
    target = Target(background, 32)
    missile = Projectile(background)
    k_miss = Projectile(background, Kalman())
    last_x_pos = target.noisy_x_pos  # The radar sends a track beam in the direction of the target with a constant rate.
    noisy_draw = np.zeros((w, 20))

    trial = True
    iters += 1

    while trial:

        # Setter en maksimal framerate på 300. Hvis dere vil øke denne er dette en mulig endring
        clock.tick(300)
        fps = clock.get_fps()
        #print(fps)

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        background.fill(0x448844)
        surf[:, 0:20, 0] = noisy_draw

        last_x_pos = target.noisy_x_pos()
        # print("last_x_pos : \t\t", last_x_pos)

        target.move()
        missile.move(last_x_pos)
        k_miss.move(last_x_pos)

        pg.draw.rect(background, (255, 200, 0), missile.rect)
        pg.draw.rect(background, (0, 200, 255), k_miss.rect)
        pg.draw.rect(background, (255, 200, 255), target.rect)

        noisy_draw[int(last_x_pos):int(last_x_pos) + 20, :] = 255
        noisy_draw -= 1
        np.clip(noisy_draw, 0, 255, noisy_draw)

        coll = missile.rect.colliderect(target.rect)
        k_coll = k_miss.rect.colliderect(target.rect)

        if coll:
            reg_score += 1

        if k_coll:
            kalman_score += 1

        oob = missile.rect.y < 20

        if oob or coll or k_coll:
            trial = False

        pg.display.flip()

    print('kalman score: ', round(kalman_score / iters, 2))
    print('regular score: ', round(reg_score / iters, 2), "\n")

pg.quit()
