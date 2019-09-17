import numpy as np

def f(x1, x2):
	(1 - x1)^2 + 100*(x2 - x1)^2

def df(x1, x2):
	return np.array([-2*(1-x1) - 200*(x2 - x1), 200*(x2 - x1)])

def ddf():
	return np.array([[202, -200], [-200, 200]])

def dg(theta, delta, x):
	return df(x[0] + theta * delta, x[1] + theta * delta)

def ddg():
	return ddf()

def gd(x_0, e):
	x_c = x_0
	i = 0
	
	while 1:
		theta_c = 0
		delta = -df(x_c[0], x_c[1])
		x_new = x_c + theta_c*delta
		x_c = x_new
		j = 0
		while j < 10: 
			j = j + 1
			theta_new = theta_c - np.linalg.inv(ddg()) @ dg(theta_c, delta, x_c)
			theta_c = theta_new
			
		print("Iteration: {}".format(i))		
		print(x_new)
		if np.linalg.norm(delta) < 0.01:
			plt.show()
			return x_c


x_0 = np.array([-1,1])
print(gd(x_0, 1))
