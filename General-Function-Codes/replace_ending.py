#!/usr/bin/env python
def skip_elements(elements):
    # Initialize variables
    new_list = []
    #new_list = []
    i = 0
    k = len(elements)
    # print(k)
    temp_list = []
    if k == 0:
        return []
    else:

        for m in range(0, k+1, 2):
            temp_list.append(m)

        # Iterate through the list
        for temp in temp_list:
            new_list.append(elements[temp])

        return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([]))  # Should be []
