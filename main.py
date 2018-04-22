from functions import *
from objects import *
import numpy as np
import matplotlib.pyplot as plt

h = [[0,0,0,0],[[0] for i in range(60)],[0,0,0,0]]

WIDTH = 800
HEIGHT = 600
DPI = 100

sigma = [[],[],[]]
x=[[],[],[],[],[],[],[]]
x_mistakes =[[],[]]

x[0] = [0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 0, 0, 0, 0, 0,
        0, 1, 0, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0]

x[1] = [0, 0, 1, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 0, 0,
        0, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 0, 1, 0]

x[2] = [0, 0, 0, 1, 0, 0, 0, 1,
        0, 0, 0, 1, 0, 0, 1, 0,
        0, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 0, 1, 0, 0,
        0, 0, 0, 1, 0, 0, 1, 0,
        0, 0, 0, 1, 0, 0, 0, 1]

x[3] = [1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 1, 0, 0, 0, 0,
        1, 0, 1, 0, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 0, 0,
        1, 0, 1, 0, 0, 0, 0, 0,
        1, 0, 0, 1, 0, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0]



x[4] = [0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0]

x[5] = [0, 1, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 0, 1, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0]

x[6] = [0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 1, 0, 0, 0, 1, 0,
        0, 1, 0, 1, 0, 0, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 0,
        0, 1, 0, 0, 0, 1, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 1, 0, 0, 0, 0, 1, 0]



x_mistakes[0] = [0, 0, 1, 0, 0, 0, 1, 0,
                 0, 0, 1, 0, 0, 1, 0, 0,
                 0, 0, 1, 0, 1, 0, 0, 0,
                 0, 0, 1, 1, 0, 0, 0, 0,
                 0, 0, 1, 1, 0, 0, 0, 0,
                 0, 0, 1, 0, 1, 0, 0, 0,
                 0, 0, 1, 0, 0, 1, 0, 0,
                 0, 0, 1, 0, 0, 0, 1, 0]

x_mistakes[1] = [0, 1, 0, 0, 0, 0, 1, 0,
                 0, 1, 1, 0, 0, 0, 1, 0,
                 0, 1, 0, 1, 0, 0, 1, 0,
                 0, 1, 0, 0, 1, 0, 1, 0,
                 0, 1, 0, 0, 0, 1, 1, 0,
                 0, 1, 0, 0, 0, 0, 1, 0,
                 0, 1, 0, 0, 0, 0, 1, 0,
                 0, 1, 0, 0, 0, 0, 1, 0]

x = add_x(x)

output_error = [[0,0,0,0],[[0] for i in range(60)],[0,0,0,0]]

nu = 0.1
b1 = 1.5
b2 = 1.5
b3 = 2
# w1 = np.random.sample((4, 35))
# w2 = np.random.sample((9,4))
# w3 = np.random.sample((6,9))

w1 = [[0] * 64 for i in range(4)]
w2 = [[0] * 4 for i in range(60)]
w3 = [[0] * 60 for i in range(4)]

epohi = 200
for i in range(4):
    for j in range(64):
        w1[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(60):
    for j in range(4):
        w2[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(4):
    for j in range(60):
        w3[i][j] = np.random.uniform(-0.5, 0.5)

e = np.zeros(epohi)
e_error = np.zeros(epohi)
t = [[1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]

t = add_t(t)
t_error = [[1,0,0,0],
           [0,0,0,1]]

def learning(x,w1,w2,w3,sigma,h,e, output_error,e_error,t, t_error,b1,b2,b3):
    for m in range(epohi):
        for j in range(len(x)):
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
    for m in range(len(x)):
        for i in range( len( h[0] ) ):
            h[0][i] = activate_function( sum_func( x[m], w1[i] ), b1 )
            output_error[0][i] = activate_function( sum_func( x_mistakes[0], w1[i] ), b1 )
        for i in range( len( h[1] ) ):
            h[1][i] = activate_function( sum_func( h[0], w2[i] ), b2 )
            output_error[1][i] = activate_function(sum_func(output_error[0],w2[i]), b2)
        for i in range( len( h[2] ) ):
            h[2][i] = round(activate_function( sum_func( h[1], w3[i] ), b3 ),3)
            output_error[2][i] = round(activate_function(sum_func(output_error[1],w3[i]), b3 ),3)
        print( "{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} ".format( h[2][0], h[2][1], h[2][2], h[2][3] ) )





def show_graph():
    len_e = []
    for i in range( epohi ):
        len_e.append( i )
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



