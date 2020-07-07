# Total Profit/Loss over period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvfile:
        sum()


# create functions
def Print_Total_Profit_Loss(csv):
    Total_Profit_Loss = int(csv[1])

Average_Change = int()
GPI =
GPD = 

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average  Change: ${Average_Change}')
print('Greatest Increase in Profits: Feb-2012 ${GPI}')
print('Greatest Decrease in Profits: Sep-2013 ${GPD}')