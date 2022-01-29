# Read in the contents of the file SP500.txt
# which has monthly data for 2016 and 2017
# about the S&P 500 closing prices as well
# as some other financial indicators,
# including the “Long Term Interest Rate”,
# which is interest rate paid on 10-year U.S. government bonds.

# Write a program that computes
# the average closing price(the second column, labeled SP500)
# and the highest long-term interest rate.
# Both should be computed only for the period
# from June 2016 through May 2017.
# Save the results in the
# variables mean_SP and max_interest.


file = open("/Users/saurabhkumarsingh/Documents/GitHub/Learning_python/UoM_Specializations/C2_Python Functions_Files_and_Dictionaries/Week_1/SP500.txt")

alllines = file.readlines()

sp = 0
interest = 0

for i in range(6, 18):
    singleline = alllines[i]
    linewords = singleline.split(",")
    singleSP = float(linewords[1])
    singleInterest = float(linewords[5])
    sp = sp + singleSP
    if singleInterest > interest:
        interest = singleInterest

mean_SP = sp/12
max_interest = interest

print(mean_SP, max_interest)

file.close()
