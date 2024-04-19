import os
import csv
election_data = os.path.join('PyPoll','Resources','election_data.csv')

print("Election Results")
print("--------------------------------")

with open('election_data.csv', 'r') as csvfile:
    row_count = 0
    for row in csvfile:
        row_count += 1
print("Total Votes: " , row_count)

vote_counts = {}

print("--------------------------------")
with open('election_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    total_votes = 0
    for row in reader:
        candidate_name = row["Candidate"]
        total_votes += 1
        
        if candidate_name in vote_counts:
            vote_counts[candidate_name] += 1
        else:
            vote_counts[candidate_name] = 1

for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    vote_counts[candidate] = {"votes": votes, "percentage": percentage}

print("Candidates who received votes:")
for candidate, details in vote_counts.items():
    print(f"{candidate}: ({details['percentage']:.2f}%) {details['votes']}")

print("--------------------------------")

vote_counts = {}

with open('election_data.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    total_votes = 0
    for row in reader:
        candidate_name = row["Candidate"]
        total_votes += 1
        
        # Update the vote count for the candidate
        if candidate_name in vote_counts:
            vote_counts[candidate_name] += 1
        else:
            vote_counts[candidate_name] = 1

# Determine the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)
winner_votes = vote_counts[winner]

# Print the winner of the election
print("Winner: {winner}")

print("--------------------------------")