
import datetime


# %%
def weight_reduce_generator():
    """generates weight corresponding to the percentage decrease
    per week given initial week and total weeks """
    # initialize variables
    x = 0
    y = 0
    z = 0

    for x in range(15):
        y = 83*(0.99)**x
        z = round(y, 1)

        # print (x,":",y)
        # print(x,':', z, ':', y)
        print(x, ':', z)


# weight_reduce_generator()
# %%
x = datetime.datetime.now()
print(x)

# %%

# %%
