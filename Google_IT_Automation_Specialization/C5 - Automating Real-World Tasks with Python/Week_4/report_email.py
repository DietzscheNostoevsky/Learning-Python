#!/usr/bin/env python3

# %%
import os
import datetime
import reports
import emails


date = datetime.date.today().strftime("%B  %d, %Y")
title = f'Processed update on {date}'
filedir = 'supplier-data/descriptions'
dirs = [os.path.join(filedir, file)
        for file in os.listdir(filedir) if file.endswith('.txt')]

#dirs = sorted(dirs)
fruits = []

for file in dirs:
    with open(file, 'r') as txt_data:
        data = txt_data.readlines()
        fruits.append((data[0].strip(), data[1].strip()))

summary = ''
br = '<br />'
for fruitname, fruitweight in fruits:
    summary += 'name: ' + fruitname + br + 'weight: ' + fruitweight + br + br


# %%
if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", title, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(
        sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

# %%
