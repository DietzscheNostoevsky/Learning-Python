# %%
file = open("/Users/saurabhkumarsingh/Documents/GitHub/Dataset/testdata.txt")

# %%
print(file.readline())
# %%
for a in range(10):
    print(file.readline())

# %%
fulltext = file.read()
print(fulltext)
# %%
file.close()
# %%
# with keyword

with open("/Users/saurabhkumarsingh/Documents/GitHub/Dataset/testdata.txt") as file:
    print(file.readline())


# readlines - gives a list
