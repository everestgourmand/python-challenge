import pandas as pd

# Load the election data
df = pd.read_csv('Resources/election_data.csv')

# Calculate total votes
total_votes = df['Ballot ID'].nunique()

# Get the list of unique candidates
candidates = df['Candidate'].unique()

# Dictionary to hold vote counts for each candidate
candidate_votes = {}

# Calculate vote counts and percentages for each candidate
for candidate in candidates:
    candidate_vote_count = df[df['Candidate'] == candidate].shape[0]
    percentage = (candidate_vote_count / total_votes) * 100
    candidate_votes[candidate] = (candidate_vote_count, percentage)

# Find the winner (candidate with the most votes)
winner = max(candidate_votes, key=lambda candidate: candidate_votes[candidate][0])

# Print Election Results to console
print("Election Results")
print("-------------------------")
print(f"Total votes cast: {total_votes}")
print("\nCandidates that received votes:")

for candidate, (vote_count, percentage) in candidate_votes.items():
    print(f"{candidate}: {vote_count} votes ({percentage:.3f}%)")

print(f"\nWinner: {winner}")

# Write the Election Results to a text file
with open('analysis/analysis.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total votes cast: {total_votes}\n")
    file.write("\nCandidates that received votes:\n")

    for candidate, (vote_count, percentage) in candidate_votes.items():
        file.write(f"{candidate}: {vote_count} votes ({percentage:.3f}%)\n")

    file.write(f"\nWinner: {winner}\n")