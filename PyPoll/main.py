# total number of votes cast
# complete list of candidates who received votes
# percentage of votes each candidate won
# total number of votes each candidate won
# the winner of the election based on popular vote

# Dependencies
import os
import csv

# set file path
csvpath = os.path.join('Resources_CSVfiles','election_data.csv')

# keys
total_voters = 0
voter_ID_list = []
candidate_list = []
master_candidate_list = []

# open and read
with open(csvpath) as infile:
    csvreader = csv.reader(infile, delimiter=',')
    header = next(csvreader)

    # total number of votes cast
    for row in csvreader:
        voter_ID = int(row[0])
        total_voters += 1 
        county = str(row[1])
        candidate = str(row[2])
        candidate_list.append(candidate)
        voter_ID_list.append(voter_ID)

# complete list of candidates who received votes
for candidate in candidate_list:
    if candidate not in master_candidate_list:
        master_candidate_list.append(candidate)

# number of votes each candidate won


# Khan = {
   # khan_percentage_votes, khan_total_votes
#}

