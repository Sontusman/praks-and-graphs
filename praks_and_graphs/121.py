import numpy as np
import math
import matplotlib.pyplot as plt
'''
m = 222*0.001 #kg
N = np.array([i for i in range(11)])
g = 9.81 
F = m*g*N

u_carbon = np.array([0, 0.115, 0.235, 0.365, 0.475, 0.615, 0.730, 0.865, 0.985, 1.100, 1.225])
u_carbon_err = np.array([7, 7, 7, 7, 7, 4, 7, 7, 4, 7, 4])/1000
u_alum = np.array([0, 0.09, 0.19, 0.28, 0.37, 0.465, 0.54, 0.655, 0.75, 0.845, 0.935])
u_alum_err = np.array([4, 11, 4, 11, 11, 16, 30, 7, 4, 7, 7])/1000
u_cuprum = np.array([0, 0.06, 0.12, 0.18, 0.235, 0.300, 0.36, 0.42, 0.48, 0.54, 0.59])
u_cuprum_err = np.array([4, 11, 11, 4, 7, 4, 4, 4, 4, 4, 7])/1000
u_steel = np.array([0, 0.04, 0.075, 0.115, 0.155, 0.195, 0.235, 0.275, 0.31, 0.35, 0.38])
u_steel_err = np.array([4, 4, 7, 7, 7, 7, 7, 7, 11, 4, 4])/1000


plt.errorbar(F, u_carbon, u_carbon_err, fmt = 'o', label = 'Углепластик')
plt.errorbar(F, u_alum, u_alum_err, fmt = 'o', label = 'Алюминий')
plt.errorbar(F, u_cuprum, u_cuprum_err, fmt = 'o', label = 'Медь')
plt.errorbar(F, u_steel, u_steel_err, fmt = 'o', label = 'Сталь')

line_carbon = u_carbon[0]+(u_carbon[-1]-u_carbon[0])/(F[-1]-F[0])*F
line_alum = u_alum[0]+(u_alum[-1]-u_alum[0])/(F[-1]-F[0])*F
line_cuprum = u_cuprum[0]+(u_cuprum[-1]-u_cuprum[0])/(F[-1]-F[0])*F
line_steel = u_steel[0]+(u_steel[-1]-u_steel[0])/(F[-1]-F[0])*F

A= [u_carbon[-1]-u_carbon[0], u_alum[-1]-u_alum[0], u_cuprum[-1]-u_cuprum[0], u_steel[-1]-u_steel[0]]/(F[-1]-F[0])

plt.plot(F, line_carbon)
plt.plot(F, line_alum)
plt.plot(F, line_cuprum)
plt.plot(F, line_steel)

print(A)

plt.legend(loc= 'upper left')

plt.xlabel("F, Н")
plt.ylabel("u(F), мм")
plt.grid(True)
plt.title("График зависимости u(F) для различных материалов балки")
plt.savefig('121_1')

'''

x = np.array([0, 2, 4, 6, 8, 10])*0.01+0.182
x_2 = np.power(x, 2)

u_x = np.array([1.230, 1.075, 0.92, 0.79, 0.68, 0.56])
u_x = np.flip(u_x)
u_x_error = np.array([4, 7, 4, 11, 11, 4])/1000

line= (u_x[0]-(u_x[-1]-u_x[0])/(x_2[-1]-x_2[0])*x_2[0])+(u_x[-1]-u_x[0])/(x_2[-1]-x_2[0])*x_2

plt.errorbar(x_2, u_x, u_x_error, fmt = 'o')
plt.grid(True)
plt.plot(x_2, line)

print((u_x[-1]-u_x[0])/1000/(x_2[-1]-x_2[0]))


plt.xlabel('x\u00B2, м\u00B2')
plt.ylabel('u(x\u00B2), мм')
plt.title("График зависимости u(x\u00B2) для углепластика")

plt.savefig('121_2')