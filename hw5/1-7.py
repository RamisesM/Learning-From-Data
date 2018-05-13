# Q1
def E_in (n):
    sigma = 0.1
    d = 8
    return (sigma**2)*(1 - (d+1)/n)
n_set = (10,25,100,500,1000)
# print ([E_in(n) for n in n_set])
# 100 starts to have an error of 0.0091...
# Answer: c

# Q2
# Curve is an hiperbolic curve
# 1 - x² + y² = 0
# Answer: d

# Q3
# This transformation holds a vc dimension of 15
# Answer: c

# Q4
import sympy
u, v = sympy.symbols('u v')
expr = (u*sympy.exp(v) - 2*v*sympy.exp(-u))**2
derivative = sympy.diff (expr, u)
# sympy.pprint(derivative, use_unicode=False)
# Answer: e

# Q5
def E(u,v):
    from numpy import exp
    return (u*exp(v) - 2*v*exp(-u))**2

def dE_dv(u,v):
    from numpy import exp
    return 2*(u*exp(v)-2*v*exp(-u))*(u*exp(v)-2*exp(-u))

def dE_du(u,v):
    from numpy import exp
    return 2*(exp(v)+2*v*exp(-u))*(u*exp(v) - 2*v*exp(-u))

def grad(u,v):
    return (dE_du(u,v), dE_dv(u,v))

u,v = [1.0,1.0]

counter = 0
eta = 0.1
while E(u,v) > 10.0**(-14):
    counter = counter+1
    u,v = [u-eta*dE_du(u,v), v-eta*dE_dv(u,v)]
# print (counter) #10
# Answer: d

# Q6
# print (u)
# print (v)
# 0.04473629039778207
# 0.023958714099141746
# Answer: e

# Q7
u,v = [1.0,1.0]
for i in range (15):
    u = u-eta*dE_du(u,v)
    v = v-eta*dE_dv(u,v)
# print (E(u,v)) #0.139
# Answer: a
