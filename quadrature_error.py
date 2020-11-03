import numpy as np

def quadrature_error_relative(x,sigma):
    relError=np.divide(sigma,x)
    relErrorSquare=np.square(relError)
    return np.sqrt( np.sum(relErrorSquare) )