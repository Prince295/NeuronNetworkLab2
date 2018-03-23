from functions import *
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

image=[]
image.append(Image.open( "Screenshot_5.jpg" ))
image.append(Image.open( "Screenshot_6.jpg" ))
image.append(Image.open( "Screenshot_7.jpg" ))
image.append(Image.open( "Screenshot_8.jpg" ))
x=[[],[],[],[]]
for m in range(4):
    width = image[m].size[0]  # Определяем ширину.
    height = image[m].size[1]  # Определяем высоту.
    pix = image[m].load()  # Выгружаем значения пикселей.


    for i in range( height ):
        for j in range( width ):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > 300):
                x[m].append(1)
            else:
                x[m].append(0)

h = [[0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0]]

WIDTH = 800
HEIGHT = 600
DPI = 100

sigma = [[],[],[]]

x_mistakes =[[],[]]

w1 = [[0] * 1024 for i in range(4)]
w2 = [[0] * 4 for i in range(15)]
w3 = [[0] * 15 for i in range(4)]

epohi = 500
for i in range(4):
    for j in range(1024):
        w1[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(15):
    for j in range(4):
        w2[i][j] = np.random.uniform(-0.5, 0.5)

for i in range(4):
    for j in range(15):
        w3[i][j] = np.random.uniform(-0.5, 0.5)

e = np.zeros(epohi)
e_error = np.zeros(epohi)

t = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]

t_error = [[1,0,0,0],
           [0,1,0,0]]

output_error = [[0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0]]

nu = 0.1
b1 = 0.6
b2 = 2
b3 = 7

x_mistakes[0] = get_mistake(x[0])
x_mistakes[1] = get_mistake(x[1])

for m in range(epohi):
    for j in range(4):
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
            output_error[0][i] = activate_function( sum_func( x_mistakes[j], w1[i] ), b1 )
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

for i in range( len( h[0] ) ):
    h[0][i] = activate_function( sum_func( x[1], w1[i] ), b1 )
    output_error[0][i] = activate_function( sum_func( x_mistakes[1], w1[i] ), b1 )
for i in range( len( h[1] ) ):
    h[1][i] = activate_function( sum_func( h[0], w2[i] ), b2 )
    output_error[1][i] = activate_function(sum_func(output_error[0],w2[i]), b2)
for i in range( len( h[2] ) ):
    h[2][i] = round(activate_function( sum_func( h[1], w3[i] ), b3 ),3)
    output_error[2][i] = round(activate_function(sum_func(output_error[1],w3[i]), b3 ),3)


print("{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} ".format(h[2][0], h[2][1], h[2][2], h[2][3] ))
print("{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} ".format(output_error[2][0], output_error[2][1], output_error[2][2], output_error[2][3]))

