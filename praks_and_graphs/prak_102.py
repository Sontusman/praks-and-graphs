import numpy as np
import matplotlib.pyplot as plt
from math import *
delta_x = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
t_3 = np.array([0.74, 0.49, 0.34, 0.28, 0.25])
t_6 = np.array([0.47, 0.3, 0.23, 0.20, 0.17])
t_9 = np.array([0.37, 0.24, 0.19, 0.16, 0.14])
a = atan(1/1197)
sin_a = sin(a)
g = 9.81


l = 0.05
v_3 = np.array([(l/t_3[i])**2 for i in range(len(t_3))])
v_6 = np.array([(l/t_6[i])**2 for i in range(len(t_6))])
v_9 = np.array([(l/t_9[i])**2 for i in range(len(t_3))])

fig, ax = plt.subplots()

plt.figure(figsize=(10, 5))

#plt.scatter(delta_x, v_3, label='\u0394h = 3mm')
plt.scatter(delta_x, v_6, label='m1 = 209.96г')
plt.scatter(delta_x, v_6, label='m2 = 260.61г')
#plt.scatter(delta_x, v_9, label='\u0394h = 9mm')


v_3_t=v_3[0]+(v_3[-1]-v_3[0])/(delta_x[-1]-delta_x[0])*(delta_x-delta_x[0])
v_6_t=v_6[0]+(v_6[-1]-v_6[0])/(delta_x[-1]-delta_x[0])*(delta_x-delta_x[0])
v_9_t=v_9[0]+(v_9[-1]-v_9[0])/(delta_x[-1]-delta_x[0])*(delta_x-delta_x[0])

alpha_3 = degrees(atan((v_3[-1]-v_3[0])/(delta_x[-1]-delta_x[0])))
alpha_6 = degrees(atan((v_6[-1]-v_6[0])/(delta_x[-1]-delta_x[0])))
alpha_9 = degrees(atan((v_9[-1]-v_9[0])/(delta_x[-1]-delta_x[0])))

#plt.plot(delta_x, v_3_t)
plt.plot(delta_x, v_6_t)
plt.plot(delta_x, v_6_t)
#plt.plot(delta_x, v_9_t)


plt.grid(True)
plt.xlabel('x, м') 
plt.ylabel('V\u00B2, м\u00B2/с\u00B2')


plt.title('График зависимости V\u00B2(x) для различных m')
plt.legend(loc = 'lower right')
plt.savefig('102_ex_3')
plt.show()


print(alpha_3, alpha_6, alpha_9)