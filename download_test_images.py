import mnist
import scipy.misc
from scipy.misc import imsave , toimage
images=mnist.test_images()
l=mnist.test_labels()
count = 0
while count < 200:
	img = toimage(scipy.misc.imresize(images[count,:,:] * -1 + 256, 1.))
	img.save(('../character_recognition/static/'+str(l[count])+'_'+str(count)+'.png'))
	count+= 1



