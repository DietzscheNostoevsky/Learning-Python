#!/usr/bin/env python3
# %%
import PIL
from PIL import Image
import os

dir = 'supplier-data/images'

# %%
files = os.listdir(dir)
# %%
imagedirs = []
for file in files:
    if file.endswith('.tiff'):
        imagedir = os.path.join(dir, file)
        imagedirs.append(imagedir)

# %%
for imagedir in imagedirs:
    image = Image.open(imagedir)
    image = image.convert('RGB').resize((600, 400))
    path = dir + '/' + imagedir[-8:-5] + '.jpeg'
    image.save(path, 'JPEG')

# %%
