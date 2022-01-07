x = 0
y = 0
z = 0


for x in range(15):
    y = 83*(0.995)**x
    #z = int(y)
    z = round(y, 1)

    #print (x,":",y)
    #print(x,':', z, ':', y)
    print(x, ':', z)
