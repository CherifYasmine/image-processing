import numpy as np

from contrast_modif import histogram_equalization, linear_transformation, saturated_transformation
from imaga_pgm_IO import readImagePgm, writeImagePgm
'''
    Read/Write testing
'''
matrix = readImagePgm('images/mona.pgm')
ly, lx = np.shape(matrix)
#writeImagePgm(matrix, ly, lx, 255, 'output_mona.pgm')

'''
    Histogram Equalization testing
'''

#matrix_eq, hist_transform = histogram_equalization(matrix)
#writeImagePgm(matrix_eq, ly, lx, 255, "mona_equalized.pgm")

'''
    Linear Transformation testing
'''
mona_linear = linear_transformation(matrix)
writeImagePgm(mona_linear, ly, lx, 255, 'mona_linear_transformed.pgm')

'''
    Satured Transformation testing
'''
mona_satured = saturated_transformation(matrix,70,100)
writeImagePgm(mona_satured, ly, lx, 255, 'mona_satured_transformed.pgm')