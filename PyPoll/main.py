import os
import csv

votes = 0

can_list = []
can_votes = {}
winner = ""
winner_votes = 0
results = ""

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

# total number of votes cast
    for row in csvreader:
        votes +=1

# list of condidates
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        can = row[2]

        if can not in can_list:
            can_list.append(can)

# calculate count and percentage of votes each candidate recieved 
    # worked with peers in study group (Daniel, Zach, Nic) and utilized Xpert Learning Assistant to work through coding issues and bugs
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        can = row[2]
        if can in can_votes:
            can_votes[can] += 1
        else:
            can_votes[can] = 1

    for can in can_list:
        vote = can_votes[can]
        perc_votes = (vote / votes) * 100
        results += f"{can} : {perc_votes:.3f}% ({vote})\n"

# winner
        if vote > winner_votes:
            winner = can
            winner_votes = vote
    print(f"{winner}")
    
    # print final election results
        # Uilized Xpert Learning Assistant to fix percentage printing issue
    print("Election Results")
    print("--------------------------------")
    print(f'Total Votes: {votes}')
    print("--------------------------------")
    print(results)
    print("--------------------------------")
    print(f'Winner: {winner}')

# output text file results to analysis folder
output_file = os.path.join('Resources', 'Analysis')
with open(output_file, 'w') as txtfile:
    results_file = csv.writer(txtfile, delimeter=',')
    results_file.writerow(["Election Results"])
    results_file.writerow(["--------------------------------"])
    results_file.writerow(['Total Votes: {votes}'])
    results_file.writerow(["--------------------------------"])
    results_file.writerow([results])
    results_file.writerow(["--------------------------------"])
    results_file.writerow([f'Winner: {winner}'])
