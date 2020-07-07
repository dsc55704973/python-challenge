# PyBank task: analyze financial data for budget_data.csv
# Total number of months
# Net total amount of Profit/Losses over entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Dependencies
import os
import csv

# Set file path
#total_months 
#month_of_change 
#net_change_list 
#greatest_increase
#greatest_decrease 
#total_net
csvpath = os.path.join('Resouces_CSVfiles','budget_data.csv')

# parameters
# dict = {} 
# profit_dict={
#    'key': 'value', 
#    'key2': 'value2'
# }
# profit_list=[value, value2]

total_months = 0
total_profit_loss = 0
profit_list=[]
profit_change_list = []
month_list=[]

# Dictionary
with open(csvpath) as infile:
    csvreader = csv.reader(infile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        month = row[0]
        total_months += 1 
        profit_loss = int(row[1])
        month_list.append(month)
        profit_list.append(profit_loss)
        total_profit_loss += profit_loss

# create new loop through profit list
for x in range(0, len(profit_list)-1):
    # subtract subsequent value within profit list from previous value
    # profit_change=profit_list[1]-profit_list[0]
    # profit_change=profit_list[86]-profit_list[85]
    profit_change=profit_list[x+1]-profit_list[x]
    # create new list for variances between values within profit list
    profit_change_list.append(profit_change)
# identify greatest increase and decrease and isolate values
# output corresponding date as well as value for greatest increase/decrease

# print(profit_change_list)

#        for profit_loss in csvreader:
#            greatest_increase = max(profit_loss)
#            greatest_decrease = min(profit_loss)


# print
greatest_increase=max(profit_change_list)
greatest_decrease=min(profit_change_list)
# for profit_change in profit_change_list:
for x in range(0, len(profit_change_list)):
# for x in [0, 1, 2, ...., 85]:
    if profit_change_list[x]==greatest_increase: 
        greatest_index=x+1

print(month_list[greatest_index])
print(total_months)
print(total_profit_loss)
# print(profit_list)
print(greatest_increase)
print(greatest_decrease)