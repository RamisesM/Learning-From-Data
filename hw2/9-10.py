from perceptron import Point, Function
import numpy
import random

def linear_regression(data_set):
    X = [point for point in data_set]
    X_transpose = numpy.transpose(X)
    Y = [target_function(point[1], point[2]) for point in data_set]
    X_dagger = numpy.matmul(numpy.linalg.inv(numpy.matmul(X_transpose, X)), X_transpose)
    return numpy.matmul(X_dagger, Y)

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

# transforming data_set
transformed_data_set = [(1, point.x, point.y, point.x*point.y, point.x**2, point.y**2) for point in data_set]

# linear regression
hipothesis_set = []
number_of_runs = 1000
for _ in range (number_of_runs):
    hipothesis = linear_regression(transformed_data_set)
    hipothesis_set += [hipothesis]
final_hypothesis = sum(hipothesis_set)/number_of_runs
# print (final_hypothesis)
# [-1.22301919 -0.02412528 -0.01123268 -0.01479336  1.93993671  1.95239155]
# closest: -1, -0.05, 0.08, 0.13, 1.5, 1.5
# Answer: a

# calculating out of sample error
number_of_runs = 1000
mean_E_out = 0
for _ in range(number_of_runs):
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
    # calculating h_set
    h_set = []
    for point in data_set:
        h_set += [numpy.sign(numpy.inner(final_hypothesis, [1, point.x, point.y, point.x*point.y, point.x**2, point.y**2]))]
    # misclassified points
    misclassified_points = 0
    for index in range(len(data_set)):
        if h_set[index] != f_set[index]:
            misclassified_points += 1
    E_out = float(misclassified_points/number_of_points)
    mean_E_out += E_out
mean_E_out = mean_E_out/number_of_runs
print (mean_E_out)
# Q10
# Answer: b
