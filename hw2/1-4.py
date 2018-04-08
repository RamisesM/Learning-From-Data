import random

class Coin:
    def __init__ (self):
        self.side = random.randint (0,1)
    def flip (self):
        self.side = random.randint (0,1)

def flip_coins (coins):
    heads_occurences = []
    for coin in coins:
        heads_occurences += [coin.side]
        for _ in range (9):
            coin.flip ()
            heads_occurences[-1] += coin.side
    return heads_occurences

def run ():
    number_of_coins = 1000
    sample_coins = [Coin() for _ in range (number_of_coins)]
    heads_occurences = flip_coins (sample_coins)
    # c_min_index = heads_occurences.index(min(heads_occurences))
    v1 = float(heads_occurences[0]/10)
    v_rand = float(heads_occurences[random.randint(0, number_of_coins-1)]/10)
    v_min = float(min(heads_occurences)/10)
    return [v1, v_rand, v_min]

number_of_runs = 1000
runs = []
for _ in range (number_of_runs):
    runs += [run ()]
v_min_column = 2
avarage_v_min = sum(run[v_min_column] for run in runs)/number_of_runs
print (avarage_v_min)

# Q1
# Answer: b
# 0.037

# Q2:
# Answer: d
# When you look for the minimum its highly probable that a run performed in a
# vicious way therefore not reflecting the out of sample frequency

# Q3
# h:
# error : m
# f:
# error : 1- l
# hit * error or error*hit
# (1-m)(1-l) + m*l
# Answer: e

# Q4
# Err = 1 -l -m +2ml = 1 - m +l(2m - 1) = 1 - m if m = 1/2
# Answer: b
# This means we have a completely noisy distribution, it is random therefore we
# can't learn shit
