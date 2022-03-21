#! /usr/bin/env python3
# %%
import os
import requests

filedir = 'supplier-data/descriptions'

# turn the data from txt to json dictionary

upload_url = 'http://[linux-instance-external-IP]/fruits'

fruit_keys = [
    'name',
    'weight',
    'description',
    'image_name'
]
upload_dict = dict()


def upload(json_file):
    requests.post(upload_url, json_file)


# %%
# creating json from txt
dirs = [os.path.join(filedir, file)
        for file in os.listdir(filedir) if file.endswith('.txt')]

dirs = sorted(dirs)

for file in dirs:
    with open(file, 'r') as txt_data:
        upload_dict = dict()
        data = txt_data.readlines()
        upload_dict['name'] = data[0].strip()
        upload_dict['weight'] = int(data[1][:3])
        upload_dict['description'] = data[2].strip()
        upload_dict['image_name'] = file.split('/')[-1].split('.')[0] + '.jpeg'
        print(upload_dict)
        # upload(upload_dict)
