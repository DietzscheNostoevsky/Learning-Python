# these are all same codes


nums = [[4, 3, 12, 10], [8, 7, 6], [
    5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]


def ret_three(inlist):
    retlist = []
    for first in nums:
        for val in first:
            if val % 3 == 0:
                retlist.append(val)
    return retlist


threes = [val for first in nums for val in first if val % 3 == 0]

# ---------------------------------------------


def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result


L = [["hi", "bye"], ["hello", "goodbye"], [
    "hola", "adios", "bonjour", "au revoir"]]

result2 = [word for sublist in L for word in sublist]

# ---------------------------------------------

# Challenge: Write code to assign to the variable class_sched
# all the values of the key important classes.
# Do this using list comprehension.

# %%
tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science",
             'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science',
             "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology',
             'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science',
             "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History',
             'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior',
             'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}


def impreturn(indict):
    retlist = []
    res1 = indict['info']
    for dic in res1:
        res3 = dic['important classes']
        for clas in res3:
            retlist.append(clas)

    return retlist


#class_sched = impreturn(tester)

# %%
class_sched = [clas for dic in tester['info']
               for clas in dic['important classes']]

print(class_sched)


# %%
