import os
import csv

# Define path to collect data
pypoll_csv = os.path.join('Resources', 'election_data2.csv')

# Assign Variables
Total_Votes = 0
Khan = 0
Correy = 0
Li = 0
Otooley = 0

# Establish lists we'll need to collect data
Candidates = ["Khan","Correy","Li","O'Tooley"]
Candidate_Totals = [Khan, Correy, Li, Otooley]

# Open the CSV
with open(pypoll_csv, 'r') as PyPoll:

    csvreader = csv.reader(PyPoll, delimiter =',')

# Skip the first line which is column titles
    header = next(csvreader)

# Iterate through each row
    for row in csvreader:

# Add 1 to the total votes each time we pass through a row
        Total_Votes +=1

# Add 1 to each candidate total
        Candidate = row[2]
        if Candidate == "Khan":
            Khan +=1

        elif Candidate == "Correy":
            Correy +=1
        
        elif Candidate == "Li":
            Li +=1

        elif Candidate == "O'Tooley":
            Otooley +=1

# Divide each candidate's total by the overall total to get their win percentage
Khan_percent = round((Khan/Total_Votes) * 100)
Correy_percent = round((Correy/Total_Votes) * 100)
Li_percent = round((Li/Total_Votes) * 100)
Otooley_percent = round((Otooley/Total_Votes) * 100)

# Identify the winner by zipping together the two lists into a dictionary and finding the max value
winner = dict(zip(Candidates,Candidate_Totals))
winner_value = max(winner, key=winner.get)

# Make the results into a variable that we can call to run
analysis = (
f"\n"
f"Election Results\n"
f"--------------------------\n"
f"Total Votes: {Total_Votes}\n"
f"--------------------------\n"
f"Khan: {Khan_percent}% ({Khan})\n"
f"Correy: {Correy_percent}% ({Correy})\n"
f"Li: {Li_percent}% ({Li})\n"
f"O'Tooley: {Otooley_percent}% ({Otooley})\n"
f"--------------------------\n"
f"Winner: {winner_value}\n"
f"--------------------------\n")

# Print the analysis variable
print(analysis)

# Write output file
output_file = os.path.join("Analysis", "pypoll.txt")

# Open a textfile and populate with the analysis data 
with open(output_file, "w", newline='') as txtfile:
    txtfile.write(analysis)