"""
Karaktersatt Obligatorisk Oppgave #1
Halil Ibrahim Keser
"""

# Brukte denne hjemmesiden til å implementere kode: https://www.kalmanfilter.net/alphabeta.html
# "Example 2 – Tracking the constant velocity aircraft in one dimension"
#
# Samme som i vårt eksempel er hastigheten konstant, den endrer seg ikke over tid. Det fremkommer en lineær funskjon.
# Y= aX + b
#
# Jeg bruker et alpa beta filter til oppgaven.
# I denne sammenheng har vi ikke en delta t (track-to-track interval is Δt") så jeg prøver ut forskjellige verdier og prøver ut.
# Samme gjelder verdiene til alpha og beta.
# Jeg velger lav alpha og beta pga stor variasjon og unøyaktighet i verdier fra noise
#
# Prøvde å få litt hjelp fra nettmøtene, men det var ingen hjelp å få på denne oppgaven.
# Prøvde både på dagmøtet og kveldsmøtet.

"""
På en god dag resulterer dette over 70%
Noen ganger havner den under 55. Altså 55% - 80%

Eksempel fra output er nederst i siden.
Treffer ganske godt på rosa rektangel sin posisjon og min predikerte/beregnede verdi
self.rect.x: 		 1072        
self._xn_n:  1080.7008569046607

Ønsker gjerne løsningsforslag på oppgaven, så jeg kan implementere Pn og r på Estimate Uncertainty.
Klarte ikke å sette opp Estimate Uncertainty selv.
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
        #print("deltax: \t\t\t", deltax)
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
        print("\nself.rect.x: \t\t", self.rect.x)

    def noisy_x_pos(self):
        pos = self.rect.x
        center = self.rect.width // 2
        noise = np.random.normal(0, 1, 1)[0]
        return pos + center + noise * 300.0


class Kalman():
    def __init__(self):
        """Initialization"""
        self._n = 0.0                # Iterasjons verdi
        self._z_n = 1.0              # Inkommende måling av range (avstand av nois som fremkommer) fra radar
        self._xn_n = 1.0             # Avstand i tid n=n. Jeg predikerer et tall
        self._xn_n_minus_1 = 1.0     # Avstand i tid n=n-1
        self._xn_n_plus_1 = 1.0      # Avstand i tid n=n+1
        """Kalman Gain"""            # Kalman gain i dette sammenheng er apha og beta
        self._Kn = 0.1
        self._alpha = 0.15              # alpha filter
        self._beta = 0.23                # beta filter
        self._delta_t = 280.0             # The track-to-track interval Δt. 1/clock.get_fps()
        """Velocity"""
        self._xdotn_n = 1.0             # Velocity/hastighet i tid n=n
        self._xdotn_n_minus_1 = 1.0     # Velocity/hastighet i tid n=n-1
        self._xdotn_n_plus_1 = 1.0      # Velocity/hastighet i tid n=n+1
        """Measurement uncertainty"""
        self._r = 1.0                   # Measurement uncertainty
        self._Pn_n = 1.0                # Extrapolated estimate uncertainty i tid n=n
        self._Pn_n_minus_1 = 1.0        # Extrapolated estimate uncertainty i tid n=n-1
        self._Pn_n_plus_1 = 1.0         # Extrapolated estimate uncertainty i tid n=n+1

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

    """Estimate Uncertainty, Measurement uncertainty, Kalman Gain"""
    def MeasurementUncertainty(self):
        self._Pn_n = (1 - self._Kn) * self._Pn_n_minus_1
        self._r = self._z_n - self._xn_n
        self._Kn = self._Pn_n_minus_1 / (self._Pn_n_minus_1 + self._r)
        self._alpha = self._Kn
        measurementUncertainty = self._Pn_n + ((self._delta_t * self._delta_t) * self._Pn_n)
        return measurementUncertainty

    def Measurement(self, zi):
        self._z_n = zi  # Setter posisjonen til target

    """The Main. Hovedfunksjon"""
    def calc_next(self, z_i):
        """Step 1: MEASURE, z_n fa innkommende verdi"""
        self.Measurement(z_i)

        """Step 2: UPDATE, State Update, estimerer current state"""
        self._xn_n = self.StateUpdateEquationPosition()
        self._xdotn_n = self.StateUpdateEquationVelocity()

        """Step 3: Prediction"""
        self._xn_n_plus_1 = self.StateExtrapolationEquation()

        """Iteration"""
        self._n += 1                            # Iterer _n iterasjons teller med 1
        self._xn_n_minus_1 = self._xn_n         # Setter forrige xn (posisjon) til nåværende xn
        self._xdotn_n_minus_1 = self._xdotn_n   # Setter forrige x dot n (hastighet) til nåværende x dot n
        # self._Pn_n_minus_1 = self._Pn_n

        # """Oppdaterer Estimate Uncertainty"""
        # self._Pn_n = self.MeasurementUncertainty()

        # print("self._xn_n: ", self._xn_n)
        # print("self._z_n: ", self._z_n)
        # print("self._xdotn_n: ", self._xdotn_n)

        return self._xn_n  # returnerer nåværende xn verdi


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
    last_x_pos = target.noisy_x_pos
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

"""
self.rect.x: 		 1072
self._xn_n:  1080.7008569046607
self._z_n:  909.9658843730549
self._xdotn_n:  6.912647549716007

self.rect.x: 		 1073
self._xn_n:  1158.162051364084
self._z_n:  1597.108819967483
self._xdotn_n:  7.336839805089039

self.rect.x: 		 1074
self._xn_n:  1080.3734290502084
self._z_n:  639.5712359382474
self._xdotn_n:  6.910854492417816

self.rect.x: 		 1075
self._xn_n:  1012.866742639842
self._z_n:  630.3288529810986
self._xdotn_n:  6.541175019218191

self.rect.x: 		 1076
self._xn_n:  1019.2859362624655
self._z_n:  1055.6613667906654
self._xdotn_n:  6.576327746199224
"""