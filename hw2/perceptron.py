import random
import numpy

class Point:
    def __init__(self):
        self.c = 1
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)
        self.vec = (self.c, self.x, self.y)

class Function:
    def __init__(self):
        self.f = [0, 0, 0]
    def randomize(self):
        points = [Point(), Point()]
        self.f[2] = -1
        self.f[1] = (points[1].y - points[0].y)/(points[1].x - points[0].x)
        self.f[0] = points[0].y - self.f[1]*points[0].x
    def classify(self, point):
        value = numpy.sign(numpy.inner(point.vec, self.f))
        if value == 0:
            value = -1
        return value

def perceptron(target_function, hypothesis, data_set):
    f_set = []
    for point in data_set:
        f_set += [target_function.classify(point)]
    h_set = []
    for point in data_set:
        h_set += [hypothesis.classify(point)]
    # misclassified points
    misclassified_set = []
    for index in range(len(data_set)):
        if h_set[index] != f_set[index]:
            misclassified_set += [index]
    number_of_iterations = 0
    while len(misclassified_set) != 0:
        test_index = misclassified_set[random.randint(0, len(misclassified_set)-1)]
        test_point = data_set[test_index]
        hypothesis.f = [hypothesis.f[i] + f_set[test_index]*test_point.vec[i] for i in range(3)]
        # updating h_set
        h_set = []
        for point in data_set:
            h_set += [hypothesis.classify(point)]
        # updating misclassified_set
        misclassified_set = []
        for index in range(len(data_set)):
            if h_set[index] != f_set[index]:
                misclassified_set += [index]
        number_of_iterations += 1
    return number_of_iterations
