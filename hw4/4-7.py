import numpy as np
import random

def target (x):
    return np.sin(np.pi * x)

class Point:
    def __init__(self):
        self.x = random.uniform(-1,1)
        self.target = target(self.x)

data_set = [Point() for _ in range(2)]

# aborted ->
# solution at:
# http://nbviewer.jupyter.org/github/tournami/Learning-From-Data-MOOC/blob/master/Homework%204.html
