import os
import csv

months = 0
total = 0
changes = []

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # specify delimiter
    csv_header = next(csvreader) # skip header row
    
    # read each row after header
    for row in csvreader:
        
    # total months
        months +=1
    print(f"Total Months: {months}")

# net total
with open(csvpath) as csvfile:
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
        total +=int(row[1])
    print(f"Total: ${total}")

# changes in profit/losses
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  
    data = list(csvreader)

for i in range(1, months):
    current_profit = int(data[i][1])
    previous_profit = int(data[i-1][1])
    change = current_profit - previous_profit
    changes.append(change)

print(f"Changes: ${changes}")

