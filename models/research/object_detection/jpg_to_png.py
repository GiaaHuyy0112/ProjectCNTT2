from PIL import Image
import os

directory = 'D:/Github/Tensorflow/models/research/object_detection/images/testjpg/'
dirsave = 'D:/Github/Tensorflow/models/research/object_detection/images/test/'
c=0
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        im = Image.open(os.path.join(directory,filename))
        name= str(c)+'.jpeg'
        rgb_im = im.convert('RGB')
        rgb_im.save(os.path.join(dirsave,name))
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue