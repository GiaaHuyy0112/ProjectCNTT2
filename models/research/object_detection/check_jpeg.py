from PIL import Image
import tensorflow as tf
import os

directory = 'D:/Github/Tensorflow/models/research/object_detection/images/testjpg/'
dirsave = 'D:/Github/Tensorflow/models/research/object_detection/images/train/'
c=0

def is_image(filename, verbose=False):

    data = open(filename,'rb').read(10)

    # check if file is JPG or JPEG
    if data[:3] == b'\xff\xd8\xff':
        if verbose == True:
             print(filename+" is: JPG/JPEG.")
        return True

    # check if file is PNG
    if data[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        if verbose == True:
             print(filename+" is: PNG.")
        return True

    # check if file is GIF
    if data[:6] in [b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61']:
        if verbose == True:
             print(filename+" is: GIF.")
        return True

    return False
	
	
for filename in os.listdir(dirsave):
    if filename.endswith(".jpg"):
        filename = os.path.join(dirsave, filename)
        name = os.path.splitext(filename)[0]
        xml = name + ".xml"
        print(is_image(filename))
        if is_image(filename, verbose=False) == False:
            ext = ".xml"
            os.remove(filename)
            if(os.path.exists(xml) == True):
                os.remove(xml)
        continue
    else:
        continue