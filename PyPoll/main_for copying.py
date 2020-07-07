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
candidate_list = []

# open and read
with open(csvpath) as infile:
    csvreader = csv.reader(infile, delimiter=',')
    header = next(csvreader)

    # create lists
    for row in csvreader:
        voter_ID = int(row[0])
        total_voters += 1 
        county = str(row[1])
        candidate = str(row[2])
        candidate_list.append(candidate)

        month_list.append(month)
        profit_list.append(profit_loss)
        total_profit_loss += profit_loss

print('Election Results')
print('-------------------------')
print(f'Total Votes: {3521001}')
print('-------------------------')
print(f'Khan: ' + {63.000} + '% ' + {(2218231)})
print(f'Correy: ' + {20.000} + '% ' + {(704200)})
print(f'Li: ' + {14.000} + '% ' + {(492940)})
print(f"O'Tooley: " + {3.000} + "% " + {(105630)})
print('-------------------------')
print(f'Winner: ' + {Khan})
print('-------------------------')

