# Q1
import numpy as np
def growth (n, d_vc):
    return n**d_vc
def confidance (epsilon, n, growth):
    # """Returns P[E_in - E_out < epsilon], means percentage of confidance""""
    return 1-4*growth*np.exp(-(n*epsilon**2)/8)

n_set = (400000, 420000, 440000, 460000, 480000)
confidance_set = []
for n in n_set:
    confidance_set += [confidance(0.05, n, growth(2*n, 10))]
# print (confidance_set)
# 460000 is the first one close to 95%
# Answer: d

# Q2
import matplotlib.pyplot as plt

N = np.linspace(start=3, stop=10000, dtype="float64")
dvc = 50
delta = 0.05

# need to take log of mH prior due to overflow error
# from Devroye bound since 4mH(N^2) --> overflow
# since mH(N) = N^dvc + 1
# log(mH(N)) is approximately dvc * log(N)

logmH = lambda constant, N, dvc: dvc * np.log(constant * N)  # approximately log(mH)

epsilon_VC = lambda N, dvc, delta: np.sqrt(8 / N * (np.log(4) + logmH(2, N, dvc) - np.log(delta)))

epsilon_rademacher = lambda N, dvc, delta: (np.sqrt(2 / N * (np.log(2 * N) + logmH(1, N, dvc))) +
                                              np.sqrt(2 / N * np.log(1 / delta)) +
                                              1 / N)

epsilon_parr_and_vdb = lambda N, dvc, delta: (1 + np.sqrt(N * (np.log(6) + logmH(2, N, dvc) - np.log(delta)) + 1)) / N

epsilon_devroye = lambda N, dvc, delta: (2 +
                                         np.sqrt(2 * N * (np.log(4) + logmH(1, N**2, dvc) - np.log(delta)) -
                                                     4 * (np.log(4) + logmH(1, N**2, dvc) - np.log(delta)) +
                                                        4)
                                        ) / (2 * (N - 2))

epsilons = [epsilon_VC(N, dvc, delta),
            epsilon_rademacher(N, dvc, delta),
            epsilon_parr_and_vdb(N, dvc, delta),
            epsilon_devroye(N, dvc, delta)]

bounds = ["Original VC bound",
          "Rademacher Penalty Bound",
          "Parrondo and Van den Broek",
          "Devroye"]

plt.title("$log(\epsilon)$ vs $N$")
plt.xlabel("$N$")
plt.ylabel("$log(\epsilon)$")

# for i in range(4):
    # take log of epsilon to zoom in!
    # plt.plot(N[-5:], np.log(epsilons[i][-5:]))
    # plt.legend(bounds,loc="best")
# plt.show()

# The graphics show that Devroye bound is the lowest
# Answer: d

N = np.float(5)
epsilons = [epsilon_VC(N, dvc, delta),
            epsilon_rademacher(N, dvc, delta),
            epsilon_parr_and_vdb(N, dvc, delta),
            epsilon_devroye(N, dvc, delta)]

bounds = ("Original VC bound",
          "Rademacher Penalty Bound",
          "Parrondo and Van den Broek",
          "Devroye")

plt.title("$\epsilon$ at $N=5$")
plt.ylabel("$\epsilon$")
plt.xticks([0.3, 1.2, 2.2, 3.4], bounds, rotation=70)

plt.bar(np.arange(4), epsilons)
plt.show()
# The graphics show that Parrondo bound is the lowest
# Answer: c
