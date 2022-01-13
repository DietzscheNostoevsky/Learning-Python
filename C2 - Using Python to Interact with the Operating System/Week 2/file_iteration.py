path = "/Users/saurabhkumarsingh/Documents/GitHub/Dataset/testdata.txt"

with open(path) as file:
    for line in file:
        print(line.upper())

with open(path) as file:
    for line in file:
        print(line.strip().lower())

print("\n")
file = open(path)

lines = file.readlines()
file.close()

lines.sort()
print(type(lines))
