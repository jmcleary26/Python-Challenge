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

# Establish lists we'll need
Candidates = ["Khan","Correy","Li","O'Tooley"]
Candidate_Totals = [Khan, Correy, Li, Otooley]

with open(pypoll_csv, 'r') as PyPoll:

    csvreader = csv.reader(PyPoll, delimiter =',')

    header = next(csvreader)

    for row in csvreader:

        Total_Votes +=1

        Candidate = row[2]
        if Candidate == "Khan":
            Khan +=1

        elif Candidate == "Correy":
            Correy +=1
        
        elif Candidate == "Li":
            Li +=1

        elif Candidate == "O'Tooley":
            Otooley +=1


Khan_percent = round((Khan/Total_Votes) * 100)
Correy_percent = round((Correy/Total_Votes) * 100)
Li_percent = round((Li/Total_Votes) * 100)
Otooley_percent = round((Otooley/Total_Votes) * 100)

winner = dict(zip(Candidates,Candidate_Totals))
winner_value = max(winner, key=winner.get)

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

print(analysis)

# Write output file
output_file = os.path.join("Analysis", "pypoll.txt")

with open(output_file, "w", newline='') as txtfile:
    txtfile.write(analysis)