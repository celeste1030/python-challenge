import os
import csv
import collections

#Make a path to the csv holding election data#

csvpath = os.path.join("Resources", "test_data.csv")

#Initialize variables#

candidates = []
candidate_votes = []
total_votes = 0

#Read csv file with csv reader#

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #For loop through rows and pull info#
    for row in csvreader:
        #Total number of votes in data set#
        total_votes += 1
    #find each candidate and print their names in candidates
        candidates.append(row[2])
    #create dictionary of candidates and number of votes#
    candidate_votes = collections.Counter(candidates)

    print(candidate_votes)

    print(total_votes)

for k, v in candidate_votes.items():
    percentage = str(round(v/total_votes * 100, 2)) + "%"

    candidate_info = [k, percentage, v]

    print(candidate_info)
    
#find winner of election#
maxvalue = max(candidate_votes.values())
winner = [k for k, v in candidate_votes.items()if v == maxvalue]
print(winner)
                
print("------------------------------")
print("Election Results")
print("------------------------------")
print(f"Total Votes:  {total_votes}")
print("------------------------------")
print(f'{candidate_info}')
print("------------------------------")
print(f'Winner:  {winner}')
print("------------------------------")
        

           

    
            
          