import matplotlib.pyplot as plt
import pandas


class Kalman:

    def __init__(self, initial_weight):
        self._n = 0
        self._z_n = initial_weight
        self._xn_n = 0.0
        self._xn_n_minus_1 = 0.0
        self._xn_n_plus_1 = 0.0
        self._K_n = 0.0
        self.listWeights = []

    def Kn(self):
        if self._n > 0:
            self._K_n = 1 / self._n
        return self._K_n

    def StateUpdateEquation(self):
        self.Kn()
        stateUpdadeEquationData = self._xn_n_minus_1 + self.Kn() * (self._z_n - self._xn_n_minus_1)
        return stateUpdadeEquationData

    def Iterate(self):
        self._n += 1
        self._xn_n_minus_1 = self._xn_n

    def Measurement(self, value):
        self._z_n = value

    def Run(self, weights):
        for weight in weights:
            self._xn_n = self.StateUpdateEquation()
            self._xn_n_plus_1 = self._xn_n
            self.listWeights.append(round(self._xn_n_plus_1, 4))
            self.Iterate()
            self.Measurement(weight)


weights = [78.2, 78.9, 78.1, 78.3, 78.4, 78.9, 78.6, 78.8, 78.7, 78.4, 79, 78.2, 78.7, 78.7, 78.3,
           78.2, 78.9, 78.1, 78.3, 78.4, 78.9, 78.6, 78.8, 78.7, 78.4, 79, 78.2, 78.7, 78.7, 78.3]
actualWeight = [78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56,
                78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56, 78.56,
                78.56, 78.56, 78.56, 78.56, 78.56, 78.56]

k = Kalman(15000)
plt.title('Kalman\nFilter')
plt.xlabel('Måling nr')
plt.ylabel('Vekt')
k.Run(weights)

print(k.listWeights)
plt.axis([0, 15, 78, 79.3])
plt.plot(k.listWeights, 'green', label='Målt')
plt.plot(actualWeight, 'orange', label='Virkelig')
plt.plot(weights, 'blue', label='Kalman')
plt.legend()
plt.show()
