from PIL import Image
import numpy as np
import os

class Fitness:
    MIN_VALUE = 0
    MAX_VALUE = 255

    curDir = os.getcwd()
    fileName = "rep.jpg"
    fn = curDir + "\\function\\" + fileName

    img = Image.open(fn)
    image = np.array(np.array(img))
    width, height = img.size

    def __init__(self):
        pass

    def fitness(self, pixel,i,j):
        z = 0
        R,G,B = np.subtract(self.image[i,j],pixel)
        z = (R + G + B)

        if(z < 0):
            z = abs(z)
            return z
        else:
            return z