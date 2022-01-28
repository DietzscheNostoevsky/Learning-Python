#! /usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds


print("welcome to this time converter")

cont = "y"

while(cont.lower() == "y"):
    hours = int(input("Enter number of Hours :"))
    minutes = int(input("Enter number of minutes :"))
    seconds = int(input("Enter number of seconds :"))

    print("Thats {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("press y for anathor conversion [y]")

print("Good Bye")
