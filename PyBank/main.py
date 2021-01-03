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

    header = next(csvreader)

    for row in csvreader:
        months.append(str(row[0]))
        profit_losses.append(int(row[1]))



    for i in range(0, len(profit_losses) -1):
        change_profit_losses.append(profit_losses[i+1]-profit_losses[i])

        
greatest_increase_profit = max(change_profit_losses)
greatest_decrease_profit = min(change_profit_losses)

greatest_increase_month = months[change_profit_losses.index(greatest_increase_profit) + 1] 
greatest_decrease_month = months[change_profit_losses.index(greatest_decrease_profit) + 1]


    # Print out the values

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
print(analysis)


# Write output file
output_file = os.path.join("Analysis", "pybank.txt")

with open(output_file, "w", newline='') as txtfile:
    txtfile.write(analysis)


# Define the function and have it accept 'pybank_data' as its sole parameter
# def print_pybank(pybank_data):
#     # Assign values to variables
#     months = str(pybank_data[0])
#     profit_losses = int(pybank_data[1])

#     # Total number of months included in the dataset
#     total_months = len(months)

#     # Net total amount of profit/losses over the entire period
#     net_total = sum(profit_losses)

#     # Average of the changes in profit/losses over the entire period
#     average_value = net_total/total_months

#     # Greatest increase in profits/losses over the entire period
#     maximum_value = max(profit_losses)
    
#     # Greatest decrease in profits/losses over the entire period
#     minimum_value = min(profit_losses)
