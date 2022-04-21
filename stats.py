import numpy as np

def mean_stdev(matrix):
    matrix = np.matrix(matrix)
    mean = matrix.mean()
    stdev = np.std(matrix)
    return mean, stdev

def histogram (matrix):
    matrix = np.matrix(matrix)
    histogram = np.zeros(256).astype(int)
    for i in range (256):
        pixels_value_i = np.sum (matrix == i )
        histogram[i] = pixels_value_i
    return histogram

def histogram_cummulated(histogram):
    histogram_c = np.zeros(256).astype(int)
    histogram_c[0] = histogram[0]
    for i in range(1,256):
      histogram_c[i] = histogram_c[i-1]+histogram[i]
    return histogram_c