from functions import *
import numpy as np
import matplotlib.pyplot as plt

h = [[0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0]]

WIDTH = 800
HEIGHT = 600
DPI = 100

sigma = [[],[],[]]
x=[[],[],[],[],[],[]]

x[0] = [0,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        0,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        0,1,1,1,0]

x[1] = [0,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        0,1,1,1,1,
        0,0,0,0,1,
        1,0,0,0,1,
        0,1,1,1,0]

x[2] = [0,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        1,0,0,0,1,
        1,0,0,0,1,
        1,0,0,0,1,
        0,1,1,1,0]

x[3] = [1,0,0,0,1,
        1,0,0,0,1,
        1,0,0,0,1,
        1,1,0,0,1,
        1,0,1,0,1,
        1,0,1,0,1,
        1,1,0,0,1,]

x[4] = [1,1,1,1,0,
        1,0,0,0,1,
        1,0,0,0,1,
        1,1,1,1,0,
        1,0,0,0,0,
        1,0,0,0,0,
        1,0,0,0,0]

x[5] = [1,0,0,1,0,
        1,0,0,1,0,
        1,0,0,1,0,
        1,0,0,1,0,
        1,0,0,1,0,
        1,1,1,1,1,
        0,0,0,0,1]
nu = 0.1
b1 = 5.5
b2 = 0.4
b3 = 1
# w1 = np.random.sample((4, 35))
# w2 = np.random.sample((9,4))
# w3 = np.random.sample((6,9))

w1 = [[0] * 35 for i in range(4)]
w2 = [[0] * 4 for i in range(9)]
w3 = [[0] * 9 for i in range(6)]

epohi = 1500
for i in range(4):
    for j in range(35):
        w1[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(9):
    for j in range(4):
        w2[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(6):
    for j in range(9):
        w3[i][j] = np.random.uniform(-0.5, 0.5)

e = np.zeros(epohi)
t = [[1,0,0,0,0,0],
     [0,1,0,0,0,0],
     [0,0,1,0,0,0],
     [0,0,0,1,0,0],
     [0,0,0,0,1,0],
     [0,0,0,0,0,1]]
for m in range(epohi):
    for j in range(6):
        for i in range(len(h[0])):
            h[0][i] = activate_function(sum_func(x[j],w1[i]) + b1)
        for i in range(len(h[1])):
            h[1][i] = activate_function(sum_func(h[0],w2[i]) + b2)
        for i in range(len(h[2])):
            h[2][i] = activate_function(sum_func(h[1],w3[i]) + b3)
        sigma[2] = get_sigma3(h,b3,t[j])
        sigma[1] = get_sigma2(h,b2,t[j],w3,sigma)
        sigma[0] = get_sigma1(h,b1,t[j],w2,sigma)
        w1 = change_weight(w1,nu,x[j],sigma[0])
        w2 = change_weight(w2,nu,x[j],sigma[1])
        w3 = change_weight(w3,nu,x[j],sigma[2])
        for i in range(len(h[2])):
            e[m]+=(h[2][i]-t[j][i])**2
len_e =[]
for i in range(epohi):
    len_e.append(i)
fig, ax = plt.subplots( num=None,
                        figsize=(WIDTH / DPI, HEIGHT / DPI),
                        dpi=DPI,
                        facecolor='w',
                        edgecolor='k' )
plt.plot(len_e,e)
plt.grid(True)
plt.legend()
plt.show()

print(h[2])

for i in range( len( h[0] ) ):
    h[0][i] = activate_function( sum_func( x[0], w1[i] ) + b1 )
for i in range( len( h[1] ) ):
    h[1][i] = activate_function( sum_func( h[0], w2[i] ) + b2 )
for i in range( len( h[2] ) ):
    h[2][i] = activate_function( sum_func( h[1], w3[i] ) + b3 )

print(h[2])