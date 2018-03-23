from functions import *
import numpy as np
import matplotlib.pyplot as plt

h = [[0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0]]

WIDTH = 800
HEIGHT = 600
DPI = 100

sigma = [[],[],[]]
x=[[],[],[],[],[],[]]
x_mistakes =[[],[]]

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

x_mistakes[0] = [0,1,1,1,0,
                 0,1,0,1,0,
                 1,0,0,0,1,
                 0,1,0,1,0,
                 1,0,1,0,1,
                 1,0,0,0,1,
                 1,0,1,1,0]

x_mistakes[1] = [0,1,0,1,0,
                 1,0,1,0,1,
                 1,0,0,0,1,
                 0,1,0,1,1,
                 0,0,1,0,1,
                 0,0,0,0,0,
                 1,1,1,1,1]

output_error = [[0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0]]

nu = 0.1
b1 = 0.6
b2 = 2
b3 = 7
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
e_error = np.zeros(epohi)
t = [[1,0,0,0,0,0],
     [0,1,0,0,0,0],
     [0,0,1,0,0,0],
     [0,0,0,1,0,0],
     [0,0,0,0,1,0],
     [0,0,0,0,0,1]]

t_error = [[1,0,0,0,0,0],
           [0,1,0,0,0,1]]

for m in range(epohi):
    for j in range(6):
        for i in range(len(h[0])):
            h[0][i] = activate_function(sum_func(x[j],w1[i]), b1)
        for i in range(len(h[1])):
            h[1][i] = activate_function(sum_func(h[0],w2[i]), b2)
        for i in range(len(h[2])):
            h[2][i] = activate_function(sum_func(h[1],w3[i]), b3)
        sigma[2] = get_sigma3(h,b3,t[j])
        sigma[1] = get_sigma2(h,b2,t[j],w3,sigma)
        sigma[0] = get_sigma1(h,b1,t[j],w2,sigma)
        w1 = change_weight(w1,nu,x[j],sigma[0])
        w2 = change_weight(w2,nu,x[j],sigma[1])
        w3 = change_weight(w3,nu,x[j],sigma[2])
        for i in range(len(h[2])):
            e[m]+=(h[2][i]-t[j][i])**2
    for j in range(2):
        for i in range( len( output_error[0] ) ):
            output_error[0][i] = activate_function( sum_func( x_mistakes[0], w1[i] ), b1 )
        for i in range( len( output_error[1] ) ):
            output_error[1][i] = activate_function( sum_func( output_error[0], w2[i] ), b2 )
        for i in range( len( output_error[2] ) ):
            output_error[2][i] = activate_function( sum_func( output_error[1], w3[i] ), b3 )
        for i in range(len(output_error[2])):
            e_error[m]+=(output_error[2][i]-t_error[j][i])**2

len_e =[]
for i in range(epohi):
    len_e.append(i)
fig, ax = plt.subplots( num=None,
                        figsize=(WIDTH / DPI, HEIGHT / DPI),
                        dpi=DPI,
                        facecolor='w',
                        edgecolor='k' )
plt.plot(len_e,e)
plt.plot(len_e, e_error)
plt.grid(True)
plt.legend()
plt.show()

print(h[2])

for i in range( len( h[0] ) ):
    h[0][i] = activate_function( sum_func( x[0], w1[i] ), b1 )
    output_error[0][i] = activate_function( sum_func( x_mistakes[0], w1[i] ), b1 )
for i in range( len( h[1] ) ):
    h[1][i] = activate_function( sum_func( h[0], w2[i] ), b2 )
    output_error[1][i] = activate_function(sum_func(output_error[0],w2[i]), b2)
for i in range( len( h[2] ) ):
    h[2][i] = round(activate_function( sum_func( h[1], w3[i] ), b3 ),3)
    output_error[2][i] = round(activate_function(sum_func(output_error[1],w3[i]), b3 ),3)


print("{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} , {4:.3f} , {5:.3f}".format(h[2][0], h[2][1], h[2][2], h[2][3], h[2][4], h[2][5] ))
print("{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} , {4:.3f} , {5:.3f}".format(output_error[2][0], output_error[2][1], output_error[2][2], output_error[2][3], output_error[2][4], output_error[2][5]))
