import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    # was wrong previously since i put this
    filesize = os.path.getsize(filename)
    # line inside the with block

    return(filesize)


print(create_python_script("program.py"))
