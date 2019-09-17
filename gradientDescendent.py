import numpy as np
from matplotlib import pyplot as plt

def f(x1, x2):
	(1 - x1)^2 + 100*(x2 - x1)^2

def df(x1, x2):
	return np.array([-2*(1-x1) - 200*(x2 - x1), 200*(x2 - x1)])

def gd(x_0, e):
	x_c = x_0
	i = 0
	while 1:
		delta = -df(x_c[0], x_c[1])
		x_new = x_c + 0.001*delta
		x_c = x_new
		#print(np.linalg.norm(delta))
		i = i + 1
		print("Iteration: {}".format(i))		
		print(x_new)
		plt.scatter(x_new[0], x_new[1])
		if np.linalg.norm(delta) < 0.001:
			plt.show()
			return x_c


x_0 = np.array([-1,1])
print(gd(x_0, 1))
