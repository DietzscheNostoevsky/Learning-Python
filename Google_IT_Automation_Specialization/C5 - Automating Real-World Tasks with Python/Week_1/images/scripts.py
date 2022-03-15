import PIL
import os
from PIL import Image

parent = 'images'

for filename in os.listdir('images'):
    savedir = '/opt/icons/' + filename + '.jpeg'
    if filename.endswith(".py"):
        continue
    else:
        path = 'images' + '/' + filename

        with Image.open(path) as img:

            img.rotate(90).resize((128, 128)).convert('RGB')
            img.save("/opt/icons/" + filename, 'JPEG')
        # except:
        # continue
