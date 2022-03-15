
#!/usr/bin/env python3

import PIL
import os
from PIL import Image

parent = 'images'

for filename in os.listdir('images'):
    savedir = '/opt/icons/' + filename
    if filename.endswith(".py"):
        continue
    elif filename.endswith('.DS_Store'):
        continue
    else:
        path = 'images' + '/' + filename

        with Image.open(path) as img:

            a = img.rotate(270).resize((128, 128)).convert('RGB')
            a.save(savedir, 'JPEG')
