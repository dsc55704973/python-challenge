# PyBank task: analyze financial data for budget_data.csv
# Total number of months
# Net total amount of Profit/Losses over entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Dependencies
import os
import csv

# Set file path
csvpath = os.path.join('Resouces_CSVfiles','budget_data.csv')

# open and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # Total Months
    Total_Months = 0
    for row in csvfile:
        if row != '':
            Total_Months += 1
    
# Total Profit/Loss over period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csvreader:  
        total += int(row[1])

print(total)