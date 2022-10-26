import numpy as np
import matplotlib.pyplot as plt


n = np.array([0,10,20,30,40,50,60])
xn_latun = np.array([12.16,
11.82,
11.31,
10.8,
10.43,
9.91,
9.27,
])/2

xn_dural = np.array([12.14,
10.6,
9.6,
8.68,
7.88,
7.09,
6.4,
])/2

xn_orgsteklo = np.array([11,
8.79,
6.74,
4.64,
1.81,
0.95,
0.56,
])/2

xn_textolit = np.array([15.8,
14.2,
12.8,
11.4,
9.6,
8.2,
6.8,
])/2

xn_rubber = np.array([
    13.1,
9.87,
7.87,
6.04,
4.48,
3.2,
2.27
])/2

n_rubber = n/10

#T_2_err = np.array([0.086, 0.025, 0.01])
n_error = np.array([0.1]*7)
fig, ax = plt.subplots()


line_xn_latun=xn_latun[0]+(xn_latun[-1]-xn_latun[0])/(n[-1]-n[0])*(n-n[0])
A_latun = (xn_latun[-1]-xn_latun[0])/(n[-1]-n[0])

line_xn_dural=xn_dural[0]+(xn_dural[-1]-xn_dural[0])/(n[-1]-n[0])*(n-n[0])
A_dural = (xn_dural[-1]-xn_dural[0])/(n[-1]-n[0])

line_xn_orgsteklo=xn_orgsteklo[0]+(xn_orgsteklo[-1]-xn_orgsteklo[0])/(n[-1]-n[0])*(n-n[0])
A_orgsteklo = (xn_orgsteklo[-1]-xn_orgsteklo[0])/(n[-1]-n[0])

line_xn_textolit=xn_textolit[0]+(xn_textolit[-1]-xn_textolit[0])/(n[-1]-n[0])*(n-n[0])
A_textolit = (xn_textolit[-1]-xn_textolit[0])/(n[-1]-n[0])

line_xn_rubber=xn_rubber[0]+(xn_rubber[-1]-xn_rubber[0])/(n_rubber[-1]-n_rubber[0])*(n_rubber-n_rubber[0])
A_rubber = (xn_rubber[-1]-xn_rubber[0])/(n_rubber[-1]-n_rubber[0])

print(A_latun, A_dural, A_orgsteklo, A_textolit, A_rubber)
plt.errorbar(n, xn_latun, n_error, label='латунь', fmt='o')
plt.plot(n, line_xn_latun)
plt.errorbar(n, xn_dural, n_error, label='дюралюминий', fmt='o')
plt.plot(n, line_xn_dural)
plt.errorbar(n, xn_orgsteklo, n_error, label='оргстекло', fmt='o')
plt.plot(n, line_xn_orgsteklo)
plt.errorbar(n, xn_textolit, n_error, label='текстолит', fmt='o')
plt.plot(n, line_xn_textolit)
plt.errorbar(n_rubber, xn_rubber, n_error, label='резина', fmt='o')
plt.plot(n_rubber, line_xn_rubber)


plt.grid(True)
plt.xlabel('n, шт') 
plt.ylabel('x(n), см')

plt.title('График зависимости x(n) от n для различных материалов')
plt.legend(loc = 'upper right')
plt.savefig('praks_and_graphs/108_5things')


A = np.array([A_dural, A_latun, A_orgsteklo, A_textolit, A_rubber])*0.01 #в метры

l = 0.03
L = 0.65
R = 0.01

k = -1*(A*l)/(4*(L+R))
print(k, "*10^{3}")