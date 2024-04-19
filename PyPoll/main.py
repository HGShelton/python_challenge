import os
import csv

votes = 0

can_list = []
can_votes = {}

# path to accept data from resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

# total number of votes cast
    for row in csvreader:
        votes +=1
    print(f'Total Votes: {votes}') #------------------------

# list of condidates
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for row in csvreader:
        can = row[2]

        if can not in can_list:
            can_list.append(can)

# # print virtical list
#     print(f"Candidates List:")
# for can in can_list:
#     print(can)

# Percentage of votes for each candidate
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",") 
    csv_header = next(csvreader)

    for can in can_list: 
    # Set initial vote count for each candidate to 0
        can_votes[can] = 0

    for vote in can_votes: 
        can_votes[vote] += 1

    for can in can_list:
        vote = can_votes[can]
        percent_votes = (vote / votes) * 100
        print(f"{can} : {percent_votes:.3f}% ({vote})")
              



        # can = row['Candidate']
        # if can in can_votes:
        #     vote_count = vote_count + 1
        # else:
        #     vote_count = 1
        # print(vote_count)
        

    # if can == can_list:
    #     vote_count = (vote_count + 1)
    # # else can not in can_list:
    # print(vote_count)


    # for name in can:
    #     if name in vote_count:
    #         vote_count[name] += 1
    #     else:
    #         vote_count[name] = 1

    #     print(vote_count)



      








