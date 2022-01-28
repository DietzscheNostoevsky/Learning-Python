import re

result = re.search(r"^(\w*), (\w*)$", "Singh, Saurabh")
print(result)
print(result[0])
print(result[1])
print(result[2])

print(f"{result[2]} {result[1]}")


def rearranged_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"


print(rearranged_name("Dostoevsky, Fyodor"))

print(rearranged_name("Dostoevsky, F.M."))
print(rearranged_name("Dostoevsky, Fyodor"))


def rearrange_name(name):
    result = re.search(r"^(\w*), ([a-zA-Z\. ]*)$", name)
    if result == None:
        return None
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)
