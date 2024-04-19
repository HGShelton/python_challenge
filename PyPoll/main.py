import os
import csv

votes = 0

can_list = []
can_votes = {}
winner = ""
winner_votes = 0

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
#     print(can) --------------------------------------------------------------

# calculate count and percentage of votes each candidate recieved 
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
        print(f"{can} : {perc_votes:.3f}% ({vote})")

# for can, votes in can_votes.items(): #-------------------------------------------
#     print(f"{can}: {votes} votes")

# winner
        if vote > winner_votes:
            winner = can
            winner_votes = vote
    print(f"{winner}")




              



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



      








