import os
import csv

# variables
voter_count = 0
candidates = []

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

# total number of votes cast
    for row in csvreader:
        voter_count +=1
    print(f'Total Votes: {voter_count}') #------------------------

# list of condidates
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    for row in csvreader:
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)

for candidate in candidates:
    print(f"Candidates List: {candidate}")









