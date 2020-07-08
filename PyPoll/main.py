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
khan_total_votes = 0
correy_total_votes = 0
li_total_votes = 0
otooley_total_votes = 0
election_results_list = []

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
for x in candidate_list:
    if str(x) == master_candidate_list[0]: 
        khan_total_votes = khan_total_votes + 1
    if str(x) == master_candidate_list[1]: 
        correy_total_votes = correy_total_votes + 1
    if str(x) == master_candidate_list[2]: 
        li_total_votes = li_total_votes + 1
    if str(x) == master_candidate_list[3]: 
        otooley_total_votes = otooley_total_votes + 1      

# percentage votes per candidate, rounded to n=3 decimal places
khan_percentage_votes = round(((khan_total_votes / total_voters) * 100), 3)
correy_percentage_votes = round(((correy_total_votes / total_voters) * 100), 3)
li_percentage_votes = round(((li_total_votes / total_voters) * 100), 3)
otooley_percentage_votes = round(((otooley_total_votes / total_voters) * 100), 3)

print(khan_percentage_votes)

# create election results list, index it to master candidate list to determine winner
election_results_list = [khan_percentage_votes,correy_percentage_votes,li_percentage_votes,otooley_percentage_votes]
index = election_results_list.index(max(election_results_list))
election_winner = master_candidate_list[index]

# output to terminal
print('Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_voters}')
print(f'-------------------------')
print(f'Khan: {khan_percentage_votes} % ({khan_total_votes})')
print(f'Correy: {correy_percentage_votes} % ({correy_total_votes})')
print(f'Li: {li_percentage_votes} % ({li_total_votes})')
print(f'OTooley: {otooley_percentage_votes} % ({otooley_total_votes})')
print(f'-------------------------')
print(f'Winner: {election_winner}')
print(f'-------------------------')


# output to text file
analysispath = os.path.join('Analysis','Analysis.txt')
with open(analysispath, mode='w') as output:
    output.write('Election Results')
    output.write(f'-------------------------')
    output.write(f'Total Votes: {total_voters}')
    output.write(f'-------------------------')
    output.write(f'Khan: {khan_percentage_votes} % ({khan_total_votes})')
    output.write(f'Correy: {correy_percentage_votes} % ({correy_total_votes})')
    output.write(f'Li: {li_percentage_votes} % ({li_total_votes})')
    output.write(f'OTooley: {otooley_percentage_votes} % ({otooley_total_votes})')
    output.write(f'-------------------------')
    output.write(f'Winner: {election_winner}')
    output.write(f'-------------------------')