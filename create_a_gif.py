import imageio.v3 as iio



filenames = ['pic1.jpg','pic2.jpg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('viral.gif',images,duration = 500, loop = 0)