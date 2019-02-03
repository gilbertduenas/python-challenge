# import modules
import os
import csv

# load csv into output_path
file = "budget_data.csv"
output = os.path.join(".", file)

# declare lists
date = []
profit_loss = []

#read the csv
with open(output, newline = "", encoding="utf8") as file:
    data = csv.reader(file, delimiter = ',')
    for row in data:
        date.append(row[0])
        profit_loss.append(row[1])

# zip lists
budget = list(zip(date, profit_loss))

# remove the headers
del date[0]
del profit_loss[0]

# convert to int
profit_loss = list(map(int, profit_loss))

#The total number of months included in the dataset
#use len
date_len = len(date)

#The net total amount of "Profit/Losses" over the entire period
#use sum
profit_loss_sum = sum(profit_loss)

#The average of the changes in "Profit/Losses" over the entire period
# declare a list to store change values
average_change = []

#loop through list starting at second index
for i in range(1, len(profit_loss)):
    #subtract the previous index from the current index and store the change to a variable
    change = profit_loss[i] - profit_loss[i-1]
    #append the change to the average change list
    average_change.append(change)
    
#calculate the average and format to two decimal places
profit_loss_average = round(sum(average_change) / len(average_change), 2)

#The greatest increase in profits (date and amount) over the entire period
date_increase_index = (average_change.index(max(average_change)))

#The greatest decrease in losses (date and amount) over the entire period
date_decrease_index = (average_change.index(min(average_change)))

# print to the console and to results.txt
print(f'''Financial Analysis
----------------------------
Total months: {date_len}
Total: ${profit_loss_sum}
Average Change: ${str(profit_loss_average)}
Greatest Increase in Profits: {date[date_increase_index + 1]} (${max(average_change)})
Greatest Decrease in Profits: {date[date_decrease_index + 1]} (${min(average_change)})''')

with open("results.txt", "w") as text:
    print(f'''Financial Analysis
----------------------------
Total months: {date_len}
Total: ${profit_loss_sum}
Average Change: ${str(profit_loss_average)}
Greatest Increase in Profits: {date[date_increase_index + 1]} (${max(average_change)})
Greatest Decrease in Profits: {date[date_decrease_index + 1]} (${min(average_change)})''', file = text)
