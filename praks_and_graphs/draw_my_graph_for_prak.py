import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x_exp = np.array([4.58, 13.74, 22.9, 32.06, 41.22]) 
y_exp = np.array([0.396, 1.123, 1.897, 2.77, 3.437])
#yerr_exp = [0.015, 0.007, 0.003, 0.003, 0.012, 0.009]

x_teor = x_exp 
y_teor = np.array([0.407, 1.219, 2.031, 2.844, 3.656])
#yerr_teor = [0.004, 0.008, 0.011, 0.015, 0.018, 0.021]

delta_a = [2.53, 7.87, 6.65, 2.6, 6]

fig, ax1 = plt.subplots()


ax1.errorbar(x_exp, y_exp, yerr=0.001, linewidth=2, capsize=2, capthick=6, label = 'экспериментальное ускорение')
ax1.errorbar(x_teor, y_teor, yerr = 0.001, linewidth=2, capsize=2, capthick=6,  label = 'расчетное ускорение')


ax2 = ax1.twinx()
ax2.errorbar(x_teor, delta_a, yerr = 0.001, linewidth=2, capsize=2, capthick=6, label = 'относительная погрешность ускорения', color = 'r')
ax2.set_ylim(0, 10, 2)

ax1.set_xlabel('delta m, г.')
ax1.set_ylabel('a, м/с\u00B2.')
ax2.set_ylabel('delta a, %')

ax1.legend(loc='right', bbox_to_anchor=(1, 0.2))
ax2.legend(loc='lower right')
plt.grid(True)
plt.savefig('ex_3.png')
plt.show()


