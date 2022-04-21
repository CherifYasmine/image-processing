import numpy as np
from binary import closing, dilatation, erosion, opening, otsu, thresholding

from contrast_modif import histogram_equalization, linear_transformation, saturated_transformation
from filters import filer_median, filer_moy, noise, signal_to_Noise_Ratio
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
# mona_linear = linear_transformation(matrix)
# writeImagePgm(mona_linear, ly, lx, 255, 'mona_linear_transformed.pgm')

'''
    Satured Transformation testing
'''
# mona_satured = saturated_transformation(matrix,70,100)
# writeImagePgm(mona_satured, ly, lx, 255, 'mona_satured_transformed.pgm')


'''
    Making Noise testing
'''
image_with_noise = noise(matrix)
#writeImagePgm(image_with_noise, ly, lx, 255, 'mona_with_noise.pgm')

'''
    Testing Filters on images with noise
'''

# writeImagePgm(filer_moy(image_with_noise), ly, lx, 255, 'mona_noise_moy_filtered.pgm')
# writeImagePgm(filer_median(image_with_noise), ly, lx, 255, 'mona_noise_median_filtered.pgm')

'''
    Testing Filters on original image
'''

# writeImagePgm(filer_moy(matrix), ly, lx, 255, 'mona_moy_filtered.pgm')
# writeImagePgm(filer_median(matrix), ly, lx, 255, 'mona_median_filtered.pgm')

'''
    Testing SNR
'''
# print(signal_to_Noise_Ratio(matrix,filer_median(image_with_noise)))
# print(signal_to_Noise_Ratio(matrix,filer_moy(image_with_noise)))

'''
    Thresholding And Otsu
'''

# writeImagePgm(thresholding(matrix, 100), ly, lx, 255, 'mona_manual_thresholding.pgm')
# writeImagePgm(otsu(matrix), ly, lx, 255, 'mona_otsu.pgm')

'''
    Erosion, Dilatation, Opening, Closing
'''
binary_image = otsu(matrix)

writeImagePgm(erosion(matrix=binary_image), ly, lx, 255, 'mona_erosion.pgm')
writeImagePgm(dilatation(matrix=binary_image), ly, lx, 255, 'mona_dilatation.pgm')
writeImagePgm(opening(matrix=binary_image), ly, lx, 255, 'mona_opening.pgm')
writeImagePgm(closing(matrix=binary_image), ly, lx, 255, 'mona_closing.pgm')
