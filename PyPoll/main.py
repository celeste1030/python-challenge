import os
import csv
import collections

#Make a path to the csv holding election data#

csvpath = os.path.join("Resources", "election_data.csv")

#Initialize variables#

candidates = []
candidate_votes = []
total_votes = 0
candidate_stuff = []

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

        candidate_stuff.append(candidate_info)

       
        
    #find winner of election#
    maxvalue = max(candidate_votes.values())
    winner = [k for k, v in candidate_votes.items()if v == maxvalue]
    print(winner)
    #print out info in terminal#
                    
    print("------------------------------")
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes:  {total_votes}")
    print("------------------------------")
    print('\n'.join(map(str, candidate_stuff)))
    print("------------------------------")
    print(f'Winner:  {winner}')
    print("------------------------------")

    #write output file with results and put in Analysis folder#

election_results = os.path.join("Analysis", "election_results.txt")
with open(election_results, "w") as outfile:
    outfile.write("------------------------------\n")
    outfile.write("Election Results\n")
    outfile.write("------------------------------\n")
    outfile.write(f"Total Votes:  {total_votes}\n")
    outfile.write("------------------------------\n")
    outfile.write('\n'.join(map(str, candidate_stuff)))
    outfile.write("\n------------------------------\n")
    outfile.write(f'Winner:  {winner}\n')
    outfile.write("------------------------------\n")

    


        

           

    
            
          