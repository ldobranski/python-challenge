# Import modules
import os
import csv

# Create variable to hold the path to csv 
csvpath = os.path.join('Resources','election_data.csv')

# Variables
candidate_list = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_votes = 0

# read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    csv_header = next(csvfile)

    # for loop to get list of candidates
    for row in csvreader:

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

# read the csvfile in again
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    csv_header = next(csvfile)

    # loop to find votes for each candidate and total votes and total 
    for row in csvreader:
        if row[2] == 'Khan':
            khan_votes += 1
        elif row[2] == 'Correy':
            correy_votes += 1
        elif row[2] == 'Li':
            li_votes += 1
        else:
            otooley_votes += 1

        # Count the total number of votes    
        total_votes += 1

    # Print total number and percentage of of votes each candidate won
    print("Election Results")
    print('----------------------------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------------------------')
    print(f'Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})')
    print(f'Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})')
    print(f'Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})')
    print(f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})")
    print('----------------------------------------')

# Find the candidate with most votes and print winner
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
    winner = "Khan"
    # print("Winner: Khan")
elif correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
    winner = "Correy"
    # print("Winner: Correy")
elif li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
    winner = "Li"
    # print("Winner: Li")
elif otooley_votes >= khan_votes and otooley_votes >= li_votes and otooley_votes >= correy_votes:
    winner = "O'Tooley"
    # print("Winner: O'Tooley")
print(f'Winner: {winner}')
print("-----------------------------------------------------------")

# Print results to output text file
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(['----------------------------------------'])
    csvwriter.writerow([f'Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})'])
    csvwriter.writerow([f'Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})'])
    csvwriter.writerow([f'Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})'])
    csvwriter.writerow([f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------------------"])