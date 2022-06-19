
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

present_weight = int(input("Input present weight, default 85 : ") or "84")
today = datetime.date.today()

print(today)


weight_reduce_generator()

# %%
