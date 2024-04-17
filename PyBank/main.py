import os
import csv

months = 0.00
total = 0.00

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv file
with open(csvpath) as csvfile:

    # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row after header
    for row in csvreader:
        
    # total months
        months +=1
    print(f"Total Months: {months}")
    
    # net total of "Profit/Losses"







    






    


