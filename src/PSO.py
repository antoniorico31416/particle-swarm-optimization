import copy
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
from function.fitness import Fitness

class Particula:
    def __init__(self, posicion, velocidad, fitness, mejorPosicion, mejorFitness):
        self.posicion = posicion
        self.velocidad = velocidad
        self.fitness = fitness
        self.mejorPosicion = mejorPosicion
        self.mejorFitness = mejorFitness

class PSO:
    def __init__(self, dimensiones, generaciones, inercia, amg, c1, c2, problema):
        self.dimensiones = dimensiones
        self.generaciones = generaciones
        self.inercia = inercia  #Coeficiente de inercia
        self.amg = amg # Este atributo nos ayudara a modificar el coeficiente de inercia
        self.c1 = c1 #Escalares, siempre seran constantes usualmente mayores a 1
        self.c2 = c2 #Escalares
        self.problema = problema
        self.maxVel = (self.problema.MAX_VALUE - self.problema.MIN_VALUE)*.2
        self.mejorFitnessGlobal = np.inf #Al inicio el mejor Fitness es infinito
        self.mejorPosicion = np.inf #Al inicio la mejor velocidad es infinito
        self.mejores = np.zeros(11) #Guardaremos el mejor fitness de la generacion 200, 400, 600, etc.
        self.width = self.problema.width
        self.height = self.problema.height
        self.poblacion = self.width * self.height
        self.particulas = [[0 for x in range(self.width)] for y in range(self.width)]

    def run(self):
        self.crearParticlas() #Creamos las particulas
        generacion = 0
        while (generacion < self.generaciones):
            for i in range(self.width):
                for l in range(self.height):
                    # Actualizamos la velocidad de cada Particula
                    for j in range(self.dimensiones):
                        self.particulas[i][l].velocidad[j] = (self.inercia * self.particulas[i][l].velocidad[j]) + \
                                                          (self.c1 * np.random.uniform(0, self.c1) * (
                                                                      self.particulas[i][l].mejorPosicion[j] -
                                                                      self.particulas[i][l].posicion[j])) + \
                                                          (self.c2 * np.random.uniform(0, self.c2) * (
                                                                      self.mejorPosicion[j] -
                                                                      self.particulas[i][l].posicion[j]))

                    # Revisamos los limites
                    for k in range(self.dimensiones):
                        if abs(self.particulas[i][l].velocidad[k]) > self.maxVel:
                            self.particulas[i][l].velocidad[k] = ((self.particulas[i][l].velocidad[k] * self.maxVel) / abs(
                                self.particulas[i][l].velocidad[k]))

                    # Actualizamos la posicion
                    self.particulas[i][l].posicion = (self.particulas[i][l].posicion + self.particulas[i][l].velocidad)

                    # Evaluamos el Fitness
                    self.particulas[i][l].fitness = self.problema.fitness(self.particulas[i][l].posicion, i,l)


                    # Actualizamos el mejor personal y global
                    if self.particulas[i][l].fitness < self.particulas[i][l].mejorFitness:
                        self.particulas[i][l].mejorPosicion = deepcopy(self.particulas[i][l].posicion)
                        self.particulas[i][l].mejorFitness = self.particulas[i][l].fitness

                    if self.particulas[i][l].mejorFitness < self.mejorFitnessGlobal:
                        self.mejorFitnessGlobal = self.particulas[i][l].mejorFitness
                        self.mejorPosicion = deepcopy(self.particulas[i][l].mejorPosicion)
            print("Generacion: ", generacion, " -> ", self.mejorFitnessGlobal)
            generacion += 1
        result = Image.new("RGB", (self.width, self.height), "white")
        pixels = result.load()
        for i in range(result.size[0]):
            for j in range(result.size[1]):
                R,G,B = self.particulas[i][j].posicion
                #R = int(abs(R))
                #G = int(abs(G))
                #B = int(abs(B))
                R = int(R)
                G = int(G)
                B = int(B)
                pixels[i, j] = R,G,B
        result.show()


    def crearParticlas(self):
        for i in range(self.width):
            for j in range(self.height):
                posicion = np.random.uniform(self.problema.MIN_VALUE, self.problema.MAX_VALUE,self.dimensiones)  # La posicion en X e Y estaran dadas por dos valores continuos uniformes entre la velocidad minima y la maxima
                velocidad = np.zeros(self.dimensiones)  # Generamos un vector de N elementos en 0 que seran la velocidad inicial
                fitness = self.problema.fitness(posicion,i,j)  # Calculamos el Fitness a partir de la posicion de la particula
                mejorPosicion =deepcopy(posicion)
                mejorFitness = deepcopy(fitness)
                particula = Particula(posicion, velocidad, fitness, mejorPosicion, mejorFitness)
                self.particulas[i][j] = particula
                # Actualizamos el mejor fitness global
                if particula.mejorFitness < self.mejorFitnessGlobal:
                    self.mejorFitnessGlobal = particula.mejorFitness
                    self.mejorPosicion = deepcopy(self.particulas[i][j].mejorPosicion)


def main():
    instancia = Fitness()
    dimensiones = 3
    pso = PSO(dimensiones, 1000, 1, 0.99, 2, 2, instancia)
    pso.run()

if __name__ == '__main__':
    main()