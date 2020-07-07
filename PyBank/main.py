# PyBank task: analyze financial data for budget_data.csv
# Total number of months
# Net total amount of Profit/Losses over entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Dependencies
import os
import csv

# Set file path
csvpath = os.path.join('Resources_CSVfiles','budget_data.csv')

# keys
total_months = 0
total_profit_loss = 0
profit_list=[]
profit_change_list = []
month_list=[]

# open and read
with open(csvpath) as infile:
    csvreader = csv.reader(infile, delimiter=',')
    header = next(csvreader)
    
    # create lists
    for row in csvreader:
        month = row[0]
        total_months += 1 
        profit_loss = int(row[1])
        month_list.append(month)
        profit_list.append(profit_loss)
        total_profit_loss += profit_loss
        

# create new loop through profit list, subtract one for end of range
for x in range(0, len(profit_list)-1):
    # subtract subsequent value within profit list from previous value
    profit_change=profit_list[x+1]-profit_list[x]
    # create new list for variances between values within profit list
    profit_change_list.append(profit_change)

# compute greatest increase/decrease
greatest_increase = max(profit_change_list)
greatest_decrease = min(profit_change_list)

# compute average change
def average(x):
    denominator = len(x)
    numerator = 0.0
    for change in x:
        numerator += change
    return numerator / denominator
average_change = average(profit_change_list)

# create index for greatest increase
for x in range(0, len(profit_change_list)):
    if profit_change_list[x] == greatest_increase: 
        greatest_increase_index = x+1

GII_month = month_list[greatest_increase_index]

# create index for greatest decrease
for x in range(0, len(profit_change_list)):
    if profit_change_list[x] == greatest_decrease: 
        greatest_decrease_index = x+1

GDI_month = month_list[greatest_decrease_index]

# output to terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average  Change: ${average_change}')
print(f'Greatest Increase in Profits: {GII_month} ${greatest_increase}')
print(f'Greatest Decrease in Profits: {GDI_month} ${greatest_decrease}')

# output to text file
analysispath = os.path.join('Analysis','Analysis.txt')
with open(analysispath, mode='w') as output:
    output.write(f'Financial Analysis')
    output.write(f'----------------------------')
    output.write(f'Total Months: {total_months}')
    output.write(f'Total: ${total_profit_loss} ')
    output.write(f'Average  Change: ${average_change}')
    output.write(f'Greatest Increase in Profits: {GII_month} ${greatest_increase}')
    output.write(f'Greatest Decrease in Profits: {GDI_month} ${greatest_decrease}')

