import os
import csv

months = 0
total = 0
greatest_inc = 0
greatest_dec = 0
changes = []
dates = []


# path to accept data from resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader) # skip header row
    
    # read each row after header
    for row in csvreader:
        
    # total months
        months +=1

# net total
with open(csvpath) as csvfile:
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
        total +=int(row[1])
        
# Used AI Xpert Learning Assistant to help debug broken code for calculating change in profit/losses
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
    dates.append(data[i][0])

# Used AI Xpert Learning Assistant to help pair date with greatest inc/dec   
# greatest increase/decrease in profits (date and amount)
    if change > greatest_inc:
        greatest_inc = change
        greatest_inc_date = data[i][0]
    elif change <greatest_dec:
        greatest_dec = change
        greatest_dec_date = data[i][0] 

# average change of profit/losses
average = sum(changes) / len(changes)

# greatest increase in profits (date and amount)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)  
    data = list(csvreader)
   

print("Finanancial Analysis")
print("--------------------------------")
print(f"Total Months: {months}") 
print(f"Total: ${total}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_date}, ${greatest_inc}")
print(f"Greatest Decrease in Profits: {greatest_dec_date}, ${greatest_dec}")
