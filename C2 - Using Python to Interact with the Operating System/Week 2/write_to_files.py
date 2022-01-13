path = "/Users/saurabhkumarsingh/Documents/GitHub/Dataset/testdata.txt"

open(path, "r")
with open(path, "r") as file:
    file.write("This is test 4  ")

# "r" mode over writes a file
# "a" mode appends to the file
