# Write a function, sublist, that takes in a list of numbers as the parameter.
# In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original
# list up until it reaches the number 5 (it should not contain the number 5).


def stop_at_four(inlist):
    count = 0
    stop = len(inlist)
    retlist = []
    num = 0
    while inlist[count] != 4:
        retlist.append(inlist[count])
        count += 1
        if count == stop:
            break

    return retlist
