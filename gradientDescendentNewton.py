import numpy as np
from matplotlib import pyplot as plt

def f(x1, x2):
	(1 - x1)^2 + 100*(x2 - x1)^2

def df(x1, x2):
	return np.array([-2*(1-x1) - 200*(x2 - x1), 200*(x2 - x1)])


def g(theta, delta, x):
	x = x + theta * delta
	return f(x[0], x[1])

def dg(theta, delta, x):
	return -2 * delta[0] * (1 - x[0] - theta * delta[0]) + 200 * (delta[1] - delta[0]) * (x[1] + theta * delta[1] - x[0] - theta * delta[0])

def ddg(delta):
	return 2 * delta[0]**2 + 200 * (delta[1] - delta[0])**2

def gd(x_0, e):
	x_c = x_0
	i = 0

	while 1:
		i = i + 1
		delta = -1 * df(x_c[0], x_c[1])
		theta_c = 0
		while abs(dg(theta_c, delta, x_c)) > 0.001 or theta_c == 0:
			theta_new = theta_c - dg(theta_c, delta, x_c) / ddg(delta)
			theta_c = theta_new

		plt.scatter(x_c[0], x_c[1])
		x_new = x_c + theta_c * delta
		x_c = x_new
		
		print("Iteration: {}".format(i))
		print("theta: {}".format(theta_c))		
		print(x_new)
		if np.linalg.norm(delta) < 0.0001:
			plt.show()
			return x_c


x_0 = np.array([-1,1])
print(gd(x_0, 1))
