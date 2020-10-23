#Import Modules
import os
import csv

#Set Variables (total number of votes, candidate list, total percentage of votes, total votes per candidate)
total_votes = 0
candidate_list = []
percent_votes = []
total_candidate_votes = []


#Set CSV File Path
csvpath = os.path.join ('/' 'Users', 'rebeccatast', 'Desktop', 'Python-Challenge', 'PyPoll', 'Resources', 'polldata.csv')

#Open and Read CSV File
with open (csvpath, newline='') as csvfile:
    #CSV Reader Specifies Delimiter & Variable that Holds Contents
    csvreader = csv.reader (csvfile, delimiter = ',')

    #Read the header row first
    csv_header = next(csvreader)
    row = next(csvreader)

    #Read each row of Data after the header
    for row in csvreader:
        #Calculate Total Number of Votes
        total_votes += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            index = candidate_list.index(row[2])
            total_candidate_votes.append(1)
        else:
            index = candidate_list.index(row[2])
            total_candidate_votes[index] += 1

    #Percent Votes 
    for votes in total_candidate_votes:
        percentage = (votes/total_votes) *100
        percentage = round(percentage)
        percentage = "%.3f%%"% percentage
        percent_votes.append(percentage)
    
    #Find Winner
    winner = max(total_candidate_votes)
    index = total_candidate_votes.index(winner)
    winning_candidate = candidates[index]

#Print
print(f"Election Results")
print(f"----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------------")
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {str(percent_votes[i])} ({str(total_candidate_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


#Set output file
output_file = csvpath = os.path.join ('/' 'Users', 'rebeccatast', 'Desktop', 'Python-Challenge','PyPoll', 'Analysis', 'poll_data.txt')

#Open File Using Write Mode 
with open (output_file, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"----------------------------------\n")
    txtfile.write()
    for i in range(len(candidate_list)):
        txtfile.write(f"{candidate_list[i]}: {str(percent_votes[i])} ({str(total_candidate_votes[i])})\n")
    txtfile.write(f"----------------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write(f"----------------------------------\n")



