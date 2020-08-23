# Import modules
import os
import csv

# create variable to hold the path to csv 
budget_csv = os.path.join('Resources', 'budget_data.csv') 

# lists to store data
month = []
pl = []
pl_change = []

#variables
total_net = 0
total_month =0
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]

# read csv
with open(budget_csv) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    #print(budget_data)

    # skip header and first month (not needed for difference calculation)
    header=next(budget_data)
    first_month = next(budget_data)

    # but set the total month and total net variables to include first month data
    total_month = total_month + 1
    total_net = total_net + int(first_month[1])
    previous_net = int(first_month[1])
    
    # Loop through rows to:
    for row in budget_data:

        # keep counting total months (total lines) in the data set
        total_month = total_month + 1
    
        # keep counting net total profit/losses over the entire period
        total_net = total_net +int(row[1])
    
        # Get the differences from month-to-month in a list
        # caluclate the change between each month
        pl_change = int(row[1])-previous_net
        
        # update previous_net variable for next month change calculation
        previous_net = int(row[1])
        
        # and then populate a list with each monthly difference 
        pl = pl + [pl_change]

        # keep a list of month-yr to correspond to each monthly change
        month = month + [row[0]]

        # find the greatest monthly increase in profits
        if pl_change > greatest_increase[1]:
            greatest_increase[0] = row[0] 
            greatest_increase[1] = pl_change

        # find the greatest monthly decrease in profits (greatest loss)
        if pl_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0] 
            greatest_decrease[1] = pl_change

    # find the average of the monthly p/l changes over the entire period 
    average_monthly_change = sum(pl)/len(pl)

print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months: {total_month}')
print(f'Total: ${total_net}')
print(f'Average Change: ${round(average_monthly_change,2)}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})')

    # print(pl)
    # print(month)
    # print(total_net)

# Export a text file with the results   
output_path = os.path.join('analysis', 'financial_results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {total_month}'])
    csvwriter.writerow([f'Total: ${total_net}'])
    csvwriter.writerow([f'Average Change: ${round(average_monthly_change,2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})'])