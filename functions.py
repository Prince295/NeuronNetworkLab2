import numpy as np
def activate_function(x):
    return 1/(1+np.exp(-x))


def sum_func(h,w):
    result = 0
    for i in range(len(h)):
        result = result + h[i]*w[i]
    return result

def get_sigma3(h,b3,t):
    sigma=[]
    for i in range(len(h[2])):
        sigma.append( (h[2][i] - t[i])*b3*h[2][i]*(1-h[2][i]))
    return sigma

def get_sigma2(h,b2,t,w3,prev_sigma):
    sigma=[]
    sum = [0,0,0,0,0,0,0,0,0]
    for i in range(len(w3)):
        for j in range(len(w3[i])):
            sum[j] += prev_sigma[2][i]*w3[i][j]
    for i in range(len(h[1])):
        sigma.append( sum[i] * b2 * h[1][i]*( 1 - h[1][i] ))

    return sigma


def get_sigma1(h, b1, t, w2, prev_sigma):
    sigma = []
    sum = [0, 0, 0, 0]
    for i in range( len( w2 ) ):
        for j in range( len( w2[i] ) ):
            sum[j] = sum[j] + prev_sigma[1][i] * w2[i][j]

    for i in range( len( h[0] ) ):
        sigma.append(sum[i] * b1 * h[0][i]*( 1 - h[0][i] ))

    return sigma

def change_weight(w,nu,x,sigma):
    for i in range(len(w)):
        for j in range(len(w[i])):
            w[i][j] = w[i][j] - nu * sigma[i] * x[j]
    return w
