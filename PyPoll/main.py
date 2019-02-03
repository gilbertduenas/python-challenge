# import modules
import os
import csv

# load csv into output_path
file = "election_data.csv"
output = os.path.join(".", file)

# declare lists
votes = []

#read the csv
with open(output, newline = "", encoding="utf8") as file:
    data = csv.reader(file, delimiter = ',')
    for row in data:
        votes.append(row[2])

# remove the headers
del votes[0]

#The total number of votes
#use len and convert to string
total_votes = len(votes)

# A complete list of candidates who received votes.
can_set = set()
for x in votes:
    can_set.add(x)
can_list = list(can_set)

# store names in variables
khan_name = can_list[0]
otooley_name = can_list[1]
li_name = can_list[2]
correy_name = can_list[3]

# The percentage of votes each candidate won.
# The total number of votes each candidate won.
# variables to store count for each candidate
khan_count = votes.count('Khan')
otooley_count = votes.count("O'Tooley")
li_count = votes.count('Li')
correy_count = votes.count('Correy')

# variables for percent calculation
khan_votes = khan_count / total_votes * 100
otooley_votes = otooley_count / total_votes * 100
li_votes = li_count / total_votes * 100
correy_votes = correy_count / total_votes * 100

# The winner of the election based on popular vote.
winner_list = [khan_count, otooley_count, li_count, correy_votes]
winner_index = winner_list.index(max(winner_list))

print(f'''Election Results
----------------------------
Total Votes: {str(total_votes)}
----------------------------
{khan_name}: {khan_votes:.3f}% ({khan_count})
{correy_name}: {correy_votes:.3f}% ({correy_count})
{li_name}: {li_votes:.3f}% ({li_count})
{otooley_name}: {otooley_votes:.3f}% ({otooley_count})
----------------------------
Winner: {can_list[winner_index]}
----------------------------''')

# save results to a file
with open("results.txt", "w") as text:

    print(f'''Election Results
----------------------------
Total Votes: {str(total_votes)}
----------------------------
{khan_name}: {khan_votes:.3f}% ({khan_count})
{correy_name}: {correy_votes:.3f}% ({correy_count})
{li_name}: {li_votes:.3f}% ({li_count})")
{otooley_name}: {otooley_votes:.3f}% ({otooley_count})
----------------------------
Winner: {can_list[winner_index]}
----------------------------''', file = text)