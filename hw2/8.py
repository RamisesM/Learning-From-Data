from perceptron import Point, Function
import numpy
import random

def linear_regression(hypothesis, data_set):
    X = [point.vec for point in data_set]
    X_transpose = numpy.transpose(X)
    Y = [target_function(point.x, point.y) for point in data_set]
    X_dagger = numpy.matmul(numpy.linalg.inv(numpy.matmul(X_transpose, X)), X_transpose)
    hypothesis.f = numpy.matmul(X_dagger, Y)

def target_function(x1, x2):
    value = numpy.sign(x1**2 + x2**2 - 0.6)
    if value == 0:
        value = -1
    return value

# generating points
number_of_points = 1000
data_set = [Point() for _ in range(number_of_points)]
# calculating target_function values
f_set = []
for point in data_set:
    f_set += [target_function(point.x, point.y)]
# generating noise
for index in random.sample(range(number_of_points), int(number_of_points/10)):
    f_set[index] = -f_set[index]
# linear regression
avarage_E_in = 0
for _ in range (1000):
    hypothesis = Function()
    linear_regression(hypothesis, data_set)
    h_set = []
    for point in data_set:
        h_set += [hypothesis.classify(point)]
    # misclassified points
    misclassified_points = 0
    for index in range(len(data_set)):
        if h_set[index] != f_set[index]:
            misclassified_points += 1
    E_in = float(misclassified_points/number_of_points)
    avarage_E_in += E_in
avarage_E_in = avarage_E_in/1000
# print (avarage_E_in)
# Q8
# Answer: d
