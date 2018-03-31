# Q1
# Answer: a -> d

# Q2
# Answer: a

# Q3
P = 2/3*1 # bag with 2 blacks (total of three blacks)
# Answer: c -> d

# Q4
# Probability of having no reds
P = 0.45**10
# print (P)
# Answer: b

# Q5
# Probability of having at least one red:
P = 1-P
# 1000 of them having at least one red:
P = P**1000
# At least one of them having at least one red
P = 1-P
# print (P)
# Answer: c

def hoeffidings(epsilon, N):
    from math import exp
    return 2*exp(-2*N*epsilon**2)

# Q6
points = (101, 110, 111)
possible_results = (0, 1)
import itertools
targets = tuple(tuple(zip(points, result)) for result in itertools.product(possible_results, repeat=3))
def g (points):
    x = points / 100
    y = (points % 100)/10
    z = points % 10
    return ((x,y,z).count(1) % 2 == 0)
score = 0
for target in targets:
    hits = 0
    for point_target in target:
        if g(point_target[0]) == point_target[1]:
            hits += 1
    score += hits
# print (score)
# a -> 12
# b-> 12
# c -> 12
# d -> 12
# Answer: e

# perceptron
from numpy import sign, inner
from random import randint

def generate_random_points(number):
    from random import uniform
    return tuple((uniform(-1,1), uniform(-1,1), 1) for _ in range(0, number))

number_of_runs = 1000
converge_iterations = []

number_of_test_points = 1000
test_data = generate_random_points(number_of_test_points)
incorrect = 0

for _ in range (0,number_of_runs):
    number_of_points = 100
    data = generate_random_points(number_of_points)
    # generating target function f
    base_points = generate_random_points(2)
    f = [(base_points[1][1] - base_points[0][1])/(base_points[1][0] - base_points[0][0])]
    f += [1]
    f += [base_points[0][1] - f[0]*base_points[0][0]]
    # generating f_set
    f_set = []
    for point in data:
        value = sign(inner(point, f))
        if value == 0:
            value = -1
        f_set += [value]
    # w vector
    w = [0, 0, 0]
    # generating h_set
    h_set = []
    for point in data:
        value = sign(inner(point, w))
        if value == 0:
            value = -1
        h_set += [value]
    # misclassified points
    bad_set = []
    for index in range(0,number_of_points):
        if h_set[index] != f_set[index]:
            bad_set += [index]
    # getting random misclassified point
    iterations = 1
    while len(bad_set) != 0:
        test_index = bad_set[randint(0, len(bad_set)-1)]
        test_point = data[test_index]
        w = [w[index] + f_set[test_index]*test_point[index] for index in range(0,3)]
        # updating h_set
        h_set = []
        for point in data:
            value = sign(inner(point, w))
            if value == 0:
                value = -1
            h_set += [value]
        # updating bad_set
        bad_set = []
        for index in range(0,number_of_points):
            if h_set[index] != f_set[index]:
                bad_set += [index]
        iterations += 1
    converge_iterations += [iterations]
    for point in test_data:
        fvalue = sign(inner(point, f))
        if fvalue == 0:
            fvalue = -1
        hvalue = sign(inner(point, w))
        if hvalue == 0:
            hvalue = -1
        if fvalue != hvalue:
            incorrect += 1

avarage_tries = sum(converge_iterations)/len(converge_iterations)

p_of_give_bad = incorrect/(number_of_test_points*number_of_runs)

# Q7
# print (avarage_tries)
# arround 15
# Answer: b

# Q8
# print(p_of_give_bad)
# arround 0.1
# Answer: c

# Q9
# print (avarage_tries)
# arround 100
# Answer: b

# Q10
# print(p_of_give_bad)
# arround 0.01
# Answer: b
