#Import modules#
import os
import csv

#Make path to join and read csv file#
csvpath = os.path.join("Resources", "budget_data.csv")


#Initialize variables#
month_count = 0
net_total = 0
avg_changes = 0


#Lists to hold variables#
total_changes = []
months = []



#Open file with csv reader#
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

#Name header#
    csv_header = next(csvreader)

#For loop through rows and pull info#
    for row in csvreader:
        
        #Total number of months in dataset#
        month_count = month_count + 1

        #Total amount of Profits/Loss#
        current_months_change = int(row[1])
        net_total = net_total + current_months_change

        #Average changes of Profits/Loss#
        if (month_count == 1):
            prev_profit = current_months_change

            
        else:
            total_change = current_months_change - prev_profit

            months.append(row[0])


            total_changes.append(total_change)
            prev_profit = current_months_change
            
            
            
    #Calculate average change and round#
    avg_change = round(sum(total_changes)/(month_count -1), 2)

    #Calculate greatest increase and greatest decrease#
    greatest_increase = max(total_changes)
    greatest_decrease = min(total_changes)

    #Find the index value of greatest increase and greatest decrease#
    greatest_increase_index = total_changes.index(greatest_increase)
    greatest_decrease_index = total_changes.index(greatest_decrease)
    
    #Find best month and worst month#
    best_month = months[greatest_increase_index]
    worst_month = months[greatest_decrease_index]
        
#Print Financial Analysis and info in Terminal#
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_total}")
print(f"Average Change:  ${avg_change}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})")

# Export results in a text file #

budget_results = os.path.join("Analysis", "budget_results.txt")
with open(budget_results, "w") as outfile:

    outfile.write("----------------------------\n")
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${net_total}\n")
    outfile.write(f"Average Change:  ${avg_change}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})\n")

#You're all set!#

