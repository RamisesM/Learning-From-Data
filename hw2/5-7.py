from perceptron import Point, Function, perceptron
import numpy

def linear_regression(target_function, hypothesis, data_set):
    X = [point.vec for point in data_set]
    X_transpose = numpy.transpose(X)
    Y = [target_function.classify(point) for point in data_set]
    X_dagger = numpy.matmul(numpy.linalg.inv(numpy.matmul(X_transpose, X)), X_transpose)
    hypothesis.f = numpy.matmul(X_dagger, Y)

# generating data set
number_of_points = 100
data_set = [Point() for _ in range(number_of_points)]
# generating target function
target_function = Function()
target_function.randomize()

f_set = []
for point in data_set:
    f_set += [target_function.classify(point)]


number_of_hypothesis = 1000
set_of_hypothesis = []
E_in = 0
for _ in range(number_of_hypothesis):
    # creating initial hypothesis through linear regression
    hypothesis = Function()
    linear_regression(target_function, hypothesis, data_set)
    set_of_hypothesis += [hypothesis]

    h_set = []
    for point in data_set:
        h_set += [hypothesis.classify(point)]
    # misclassified points
    misclassified_set = []
    for index in range(len(data_set)):
        if h_set[index] != f_set[index]:
            misclassified_set += [index]
    E_in += float(len(misclassified_set)/number_of_points)
E_in = E_in/number_of_hypothesis
# print (E_in)
# Q5
# Answer: c
number_of_points = 1000
out_data_set = [Point() for _ in range(number_of_points)]
f_set = []
for point in out_data_set:
    f_set += [target_function.classify(point)]
E_out = 0
for index in range(number_of_hypothesis):
    h_set = []
    for point in out_data_set:
        h_set += [set_of_hypothesis[index].classify(point)]
    # misclassified points
    misclassified_set = []
    for index in range(len(out_data_set)):
        if h_set[index] != f_set[index]:
            misclassified_set += [index]
    E_out += float(len(misclassified_set)/number_of_points)
E_out = E_out/number_of_hypothesis
# print (E_out)
# Q6
# Answer: c

number_of_iterations = 0
for _ in range (1000):
    # generating data set
    number_of_points = 10
    data_set = [Point() for _ in range(number_of_points)]
    # generating target function
    target_function = Function()
    target_function.randomize()
    # linear regression
    hypothesis = Function()
    linear_regression(target_function, hypothesis, data_set)
    # perceptron
    number_of_iterations += perceptron(target_function, hypothesis, data_set)
number_of_iterations = number_of_iterations/1000
# print (number_of_iterations)
# Q7
# Answer: a
