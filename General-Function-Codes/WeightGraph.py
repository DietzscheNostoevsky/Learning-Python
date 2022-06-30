
import datetime


# %%
def weight_reduce_generator():
    """generates weight corresponding to the percentage decrease
    per week given initial week and total weeks """
    # initialize variables
    x = 0
    y = 0
    z = 0
    t = today
    # add variables to account for calories

    print("Today's date is : ", today)

    for x in range(0, 130, 7):

        y = present_weight*(0.999)**x
        z = round(y, 1)

        # print (x,":",y)
        # print(x,':', z, ':', y)

        #print(x, ':', z)
        t = today + datetime.timedelta(x)
        print(t, ':', z)


print("Welcome to Weight Reduce Generator")
print("It shows how much weight you will lose in coming days")
print("If you lose 1 % of your weight per week")

present_weight = float(
    input("Input present weight, default 84.5 : ") or "84.5")
today = datetime.date.today()

print(today)


weight_reduce_generator()

# %%
# add functionality for 1 percent and 0.5 percent per week loss
# How to come to 0.999 vs 0.995 vs 0.99 ?
# add input for 0.5 vs 1 percent per week
