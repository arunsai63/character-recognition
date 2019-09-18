from bottle import route, run, get, post, template, static_file, request
import random
import os
import numpy as np
from PIL import Image
import mnist
import scipy.spatial.distance


#home() serves the home page(i.e index.html page on start).
@get("/")
def home():
    return template("index")


#send_static(filename) serves the files present in the static folder.
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root = 'static/')


#shuffle() serves the main page, it shuffles the images randomly and displays them
#this code requires a minimum of 30 pictures present in the static folder.
@get("/page")
def shuffle():
    files = os.listdir('static/')
    files.remove('index_pic.png')
    files.remove('.gitignore')
    random.shuffle(files)
    return template("page", a = files[:30])


#When the user upload an image, this do_upload() saves the image in the static folder named as 'pic.png'.
#the default K value is 60 & the default train_images value is 60,000.
@post('/recognise')
def do_upload():
    upload = request.files.get('upload')
    if request.forms.get("k1") == "":
        k = 60
    else:
        k = int(request.forms.get("k1"))
    if request.forms.get("train_samples1") == "":
        train_samples = 60000
    else:
        train_samples = int(request.forms.get("train_samples1"))
    if 'pic.png' in os.listdir('static/'):
        os.remove('static/pic.png')
    upload.save('static/pic.png')
    result = recognise('pic.png', k, train_samples)
    return template("result", res = result)


#When the user clicks any button(image), on_click() will get the value of that buttom and also the K, train_images values
#the default K value is 60 & the default train_images value is 60,000.
@route('/button/<num>')
def on_click(num):
    if request.forms.get("k2") == None:
        k = 60
    else:
        k = int(request.forms.read("k2"))
        #print(k)
    if request.forms.get("train_samples2") == None:
        train_samples = 60000
    else:
        train_samples = int(request.forms.read("train_samples2"))
        #print(train_samples)
    result = recognise(num, k, train_samples)
    return template("result", res = result)


#load_image() takes the image location, converts it into 28 * 28 resolution images,
#converts that image into 2D array(Greyscale) & returns the 2D array.
def load_image(imgname) :
    img = Image.open(imgname)
    img = img.resize((28, 28), Image.ANTIALIAS)
    pic_as_array = np.asarray(img).reshape(28 * 28)
    return pic_as_array


#recognise take the image name, K value & train_samples values.
#It converts the image to 2D array using load_image and it converts that 2D array into a list.
#It compares that with the training_images and takes the top K closest images
#It returns the top 3 closest images with their frequencies.
def recognise(name, k, train_samples):
    pic = load_image('static/' + name)
    dist = []
    images = mnist.train_images()
    for count in range(train_samples):
        img = images[count].reshape(28 * 28)
        dist.append(scipy.spatial.distance.cosine(img, pic))
    min_dist = np.argsort(dist)
    train_labels = mnist.train_labels()
    result = [train_labels[x] for x in min_dist[:k]]
    frequencies = {x : result.count(x) for x in result}
    frequencies = sorted(frequencies.items(), key = lambda x : x[1], reverse = True)
    results = []
    for i in range(3):
        results += (frequencies[i])
    print(results)
    return results


run(host = "localhost", reloader = "True", port = 8000)
