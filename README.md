#   **Handwritten Character Recognition System:** </center>
 
##  **Introduction:**   
   Handwriting recognition has been one of the active and challenging research areas in the field of image processing and pattern recognition. It has numerous applications which include, reading aid for blind, visiting cards and conversion of any hand written document into structural text form. In this project an attempt is made to recognize handwritten characters for Digits. Each character data set contains 10 digits for Numeric data.The results show that the proposed system recognizes characters from the image in a efficient manner and provides results to user in structural text form.
  
##   **Online Handwriting Recognition:**    
                                      
In an online handwriting recognition system the motion of the tip of the stylus (pen) is sampled at equal time intervals using a digitizer tablet and it is passed to a computer which runs the handwriting recognition algorithm. In most systems, the data signal undergoes some iteration process. Then the signal is normalized to a standard size and its slant and slope is corrected. After normalization, the writing is usually segmented into basic units and each segment is classified and labeled. Using a search algorithm in the context of a language model, the most likely path is then returned to the user as the intended string.

![alt text](http://3.imimg.com/data3/XG/YK/MY-6744174/intelligent-character-recognition-250x250.jpg)

##   **Tech Stack:**   
- We used web basics like HTML, CSS from [W3 Schools]https://www.w3schools.com
- python from [Python Tutorial]https://www.tutorialspoint.com/python/index.htm  

    Installation:
    $ sudo apt install python3
- pip from [pip]https://pypi.org

    Installation:
    $ sudo apt install python3 -pip

- Bottle from [bottle]https://bottlepy.org/docs/dev/

    Installation:
    $ sudo pip3 install bottle

- mnist from [mnist dataset]https://github.com/datapythonista/mnist

    Installation:
    pip3 install mnist
  
   mnist: Python utilities to download and parse the MNIST dataset

####   mnist data set

   The mnist database is available at [http://yann.lecun.com/exdb/mnist/]

  The MNIST database is a dataset of handwritten digits. It has 60,000 training
  samples, and 10,000 test samples. Each image is represented by 28x28 pixels, each
  containing a value 0 - 255 with its grayscale value.

   ![](https://github.com/datapythonista/mnist/raw/master/img/samples.png)

   It is a subset of a larger set available from NIST.
   The digits have been size-normalized and centered in a fixed-size image.
 
   It is a good database for people who want to try learning techniques and pattern recognition
   methods on real-world data while spending minimal efforts on preprocessing and formatting.

   There are four files available, which contain separately train and test, and images and labels.

   Thanks to Yann LeCun, Corinna Cortes, Christopher J.C. Burges.

###   Usage

  mnist makes it easier to download and parse MNIST files.

  To automatically download the train files, and display the first image in the
  dataset, you can simply use:

  ```
  import mnist
  import scipy.misc

  images = mnist.train_images()
  scipy.misc.toimage(scipy.misc.imresize(images[0,:,:] * -1 + 256, 10.))
  ```

  ![](https://github.com/datapythonista/mnist/raw/master/img/img_5.png)

  Test files and labels can be downloaded in a similar way:

  ```
  import mnist

  train_images = mnist.train_images()
  train_labels = mnist.train_labels()

  test_images = mnist.test_images()
  test_labels = mnist.test_labels()
  ```

 The dataset is downloaded and cached in your temporary directory, so, calling
 the functions again, is much faster and doesn't hit the server.

 Images are returned as a 3D numpy array (samples * rows * columns). To train
 machine learning models, usually a 2D array is used (samples * features). To
 get it, simply use:

 ```
import mnist

train_images = mnist.train_images()
x = images.reshape((images.shape[0], images.shape[1] * images.shape[2]))
```
 -   scipy from [scipy]https://www.scipy.org
 -   pillow:https://pypi.org/project/Pillow/ 
                                                                   
   Installation:   
    1.pip3 install scipy   
    2.pip3 install numpy   
    3.pip3 install pillow     
 - scipy contains additional routines needed in scientific work:for example, routines for computing integrals numerically, solving differential equations, optimization, and sparse matrices.   
 - Numpy:   
Numpy is the fundamental package for scientific computing with Python.    
                                                                                                    
Installation:
- Note if pip is installed in your system:     
python -m pip install --user numpy scipy
- Ubuntu & Debian:   
sudo apt-get install python-numpy python-scipy   
- Pillow:   
Pillow is a fork of PIL (Python Image Library), started and maintained by Alex Clark and Contributors. It was based on the PIL code, and then evolved to a better, modern and more friendly version of PIL. It adds support for opening, manipulating, and saving many different image file formats. A lot of things work the same way as the original PIL.      
   
  Installation: $ sudo pip install Pillow           
   





