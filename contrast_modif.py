from stats import histogram, histogram_cummulated
import numpy as np

def histogram_equalization(matrix):
    hist = histogram(matrix)
    histC = histogram_cummulated (hist)
    hist_transform = np.zeros(256).astype(np.uint8)
    N, M = matrix.shape
    # create the image to store the equalised version
    matrix_eq = np.zeros([N,M]).astype(np.uint8)
    for z in range(256):
        s = ((255)/float(M*N))*histC[z]
        matrix_eq[ np.where(matrix == z) ] = s
        hist_transform[z] = s
    return (matrix_eq, hist_transform)

def linear_transformation(matrix):
    matrix = np.matrix(matrix)
    max = matrix.max()
    min = matrix.min()
    matrix_transformed = (255/(max-min))*(matrix-min)
    return matrix_transformed

def saturated_transformation(matrix, min, max):
    matrix = np.matrix(matrix)
    matrix_transformed = (255/(max-min))*(matrix-min)
    return matrix_transformed