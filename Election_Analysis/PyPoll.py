# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each cadidate won
# 4. The total of vote each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
print(os.getcwd())

file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")
print(os.getcwd())
print(file_to_load)

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(".\Aa\election_results.csv") as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
 
    print(headers)

