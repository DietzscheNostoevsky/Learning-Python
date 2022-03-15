from tkinter import Image
import PIL
import os
from PIL import Image

dir = 'images'
for file in os.listdir(dir):
    path = os.path.join(dir, file)
    img = Image.open(path)
    print(img.format)
