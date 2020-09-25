#import modules#
import os
import csv

#make path to join and read csv file#
csvpath = os.path.join("Resources", "budget_data.csv")

print(csvpath)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
#next column#
    csv_header = next(csvreader)
    #make lists to hold answers#
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []


