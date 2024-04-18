import os
import csv

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        
