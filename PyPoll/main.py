import csv
import os

# File paths
input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "election_results.txt")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(input_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    for row in reader:
        total_votes += 1
        candidate = row[2]

        # Count the vote
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and determine the winner
winner = ""
max_votes = 0

output_lines = []
output_lines.append("Election Results")
output_lines.append("-------------------------")
output_lines.append(f"Total Votes: {total_votes}")
output_lines.append("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > max_votes:
        max_votes = votes
        winner = candidate

output_lines.append("-------------------------")
output_lines.append(f"Winner: {winner}")
output_lines.append("-------------------------")

# Print to terminal
for line in output_lines:
    print(line)

# Write to text file
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as file:
    for line in output_lines:
        file.write(line + "\n")
