import os
import csv
budget_data = os.path.join('..','Resources', 'budget_data.csv')

print("Financial Analysis")
print("-----------------------------------")


with open('budget_data.csv','r') as csvfile: 
    row_count = 0
    for row in csvfile:
        row_count += 1
print("Total Months:", row_count - 1)


total_sum = 0

try:
    with open('budget_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  
        for row in csvreader:
            total_sum += float(row[1])
    print(f"Total: {total_sum}")

except ValueError:
    print("An error occurred while converting to float.")  


with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)
    
    total_change = 0
    count = 0
    previous_value = None
    
    for row in csvreader:
        current_value = float(row[1])
        
        if previous_value is not None:
            change = current_value - previous_value
            total_change += change
            count += 1
        
        previous_value = current_value

if count > 0:
    average_change = total_change / count
    print(f"Average Change: {average_change}")
else:
    print("No data or only one data point to calculate the change")

max_increase = 0
max_increase_date = None

with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader)
    
    previous_profit = None
    
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        
        if previous_profit is not None:
            profit_increase = profit - previous_profit
            
            if profit_increase > max_increase:
                max_increase = profit_increase
                max_increase_date = date
        
        previous_profit = profit

if max_increase_date is not None:
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
else:
    print("No profit data to calculate the increse")


greatest_decrease_amount = 0
greatest_decrease_date = ""

with open('budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    first_row = True
    
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
        
        if first_row:
            previous_profit_loss = profit_loss
            first_row = False
            continue
        
        profit_decrease = profit_loss - previous_profit_loss
        
        if profit_decrease < greatest_decrease_amount:
            greatest_decrease_amount = profit_decrease
            greatest_decrease_date = date
        
        previous_profit_loss = profit_loss

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

