import os
import csv

# Define path to collect data
pybank_csv = os.path.join('Resources','budget_data.csv')

# Assign variables as lists
months = []
profit_losses = []
change_profit_losses = []

# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Skip the first row which is column titles
    header = next(csvreader)

# Iterate through each row identifying the months as the first column and the profit/losses as the second column
    for row in csvreader:
        months.append(str(row[0]))
        profit_losses.append(int(row[1]))

# Enter another for loop to subtract the current row's profit/losses from the next row's value
    for i in range(0, len(profit_losses) -1):
        change_profit_losses.append(profit_losses[i+1]-profit_losses[i])

# Establish the maximum and minimum values from the change list
greatest_increase_profit = max(change_profit_losses)
greatest_decrease_profit = min(change_profit_losses)

# Index into the list to pull out the month value of those max and min values (add 1 because python is zero based)
greatest_increase_month = months[change_profit_losses.index(greatest_increase_profit) + 1] 
greatest_decrease_month = months[change_profit_losses.index(greatest_decrease_profit) + 1]

# Make the results into a variable that we can call to run
analysis = (
f"\n"
f"Financial Analysis\n"
f"--------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${sum(profit_losses)}\n"
f"Average Change: ${round(sum(change_profit_losses)/len(change_profit_losses),2)}\n"
f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})\n"
f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})\n"
)
# Print the values
print(analysis)

# Write output file
output_file = os.path.join("Analysis", "pybank.txt")

# Open a text file and populate with the analysis data
with open(output_file, "w", newline='') as txtfile:
    txtfile.write(analysis)
