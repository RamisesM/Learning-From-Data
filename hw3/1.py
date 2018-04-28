import numpy

# Q1
epsilon = 0.05
N = (numpy.log(2) - numpy.log(0.03))/(2*epsilon**2)
# print (N)
# ~ 840 -> 1000
# Answer: b

# Q2
epsilon = 0.05
M = 10
N = (numpy.log(2*M) - numpy.log(0.03))/(2*epsilon**2)
# print (N)
# ~ 1300 -> 1500
# Answer: c

# Q3
epsilon = 0.05
M = 100
N = (numpy.log(2*M) - numpy.log(0.03))/(2*epsilon**2)
print (N)
# ~ 1760 -> 2000
# Answer: d

# Q4
# Answer: b

# Q5
# Has to be polynomial, 2**N is the upper boundary
# Answer: b

# Q6
# 3 points-> trivial
# 4 points -> cant split 3 segments of +1
# 1 2 3 4 5
# 1 0 1 0 1 -> impossible -> 3 segments of +1
# Answer: c

# Q7
# 4 points in N+1 spaces case we have 4,3 areas 0,1,0,1 e.g
# 2 points in N+1 spaces case we have 2 areas
# 0 points in N+1 spaces case we have only one area -> 1
# Answer: c

# Q8
# In N+1 spaces we put M+1 zones so thats impossible to cover
# This means:
# C_{N+1,2M+2} = 1
# (N+1)! = (2M+2)!(N-1-2M)!
# if N = 2M+1
# (2M+2)! = (2M+2)!
# Answer: d

# Q9
# 7 You can, 8 not, one that should be out ends up being in
# Answer: d

# Q10
# Its the linear interval in 2d due to the restrictions
# The groth function is the same calculated in Q6 for 1 interval
# Answer: b
