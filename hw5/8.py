import random

class Point:
    def __init__ (self, target = lambda x: 1):
        self.x = (1, random.uniform(-1,1), random.uniform(-1,1))
        self.y = target(self.x)

def target(point, f = []):
  if f == []:
    base_points = [Point() for _ in range(2)]
    f += [1]
    f += [(base_points[0].x[2] - base_points[1].x[2]) /
          (base_points[0].x[1] * base_points[1].x[2] -
           base_points[0].x[2] * base_points[1].x[1])
          ]
    f += [(base_points[1].x[1] - base_points[0].x[1]) /
          (base_points[0].x[1] * base_points[1].x[2] -
           base_points[0].x[2] * base_points[1].x[1])
          ]
  import numpy as np
  sign = np.sign(np.inner(f, point))
  if sign == 0:
    return -1
  else:
    return sign

def gradient(data_set, w):
    import numpy as np
    grad = []
    for i in range(len(w)):
        grad += [0]
        for point in data_set:
            grad[i] += point.y*point.x[i]/(1 + np.exp(point.y*point.x[i]*w[i]))
        grad[i] = -grad[i]/len(data_set)
    return grad

# Generating data set
number_of_points = 100
data_set = [Point(target) for _ in range (number_of_points)]
w = [0]*3
print (gradient(data_set, w))
