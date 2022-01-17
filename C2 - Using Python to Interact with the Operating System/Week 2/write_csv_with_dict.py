# %%
import os
import csv
import pandas

# %%
with open("software.csv") as software:
    reader1 = csv.DictReader(software)
    for row in reader1:
        print(("{} has {} users").format(row["name"], row["users"]))

# %%

users = [{"name": "Saurabh Singh", "username": "SKS", "department": "IT Infra"},
         {"name": "Junglee Kumar", "username": "JKK", "department": "User Exp res"},
         {"name": "Piggy Piglet", "username": "PPG", "department": "developement"}]

keys = ["name", "username", "department"]


# %%

with open("by_dept.csv", "w") as dept:
    writer1 = csv.DictWriter(dept, fieldnames=keys)
    writer1.writeheader()
    writer1.writerows(users)
# %%
df = pandas.read_csv('by_dept.csv')
print(df)

# %%
