from math import *
delta_x = [0.2, 0.4, 0.6, 0.8, 1.0]
t_3 = [0.74, 0.49, 0.34, 0.28, 0.25]
t_6 = [0.47, 0.3, 0.23, 0.20, 0.17]
t_9 = [0.37, 0.24, 0.19, 0.16, 0.14]
a = atan(1/1197)
sin_a = sin(a)
g = 9.81
v = [sqrt(2*g*sin_a*delta_x[i]) for i in range(len(delta_x))]

l = 0.05
v_3 = [(l/t_3[i])**2 for i in range(len(t_3))]
v_6 = [(l/t_6[i])**2 for i in range(len(t_6))]
v_9 = [(l/t_9[i])**2 for i in range(len(t_3))]
print(v_6)