#Import Modules
import os
import csv

#Set Variables (total months, net total of profits/losses, change by month, greatest increase in profits, greatest increase in profits month, greatest decrease in profits, greatest decrease in profits month)
total_months = 0
net_total = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Set Path for CSV File
csvpath = os.path.join ('/' 'Users', 'rebeccatast', 'Desktop', 'Python-Challenge', 'PyBank', 'Resources', 'bankdata.csv')

#Open and Read CSV File
with open (csvpath, newline='') as csvfile:

    #CSV Reader Specifies Delimiter & Variable that Holds Contents, CSV.Reader tells the system where to look for the informaiton in the parentheses
    csvreader = csv.reader (csvfile, delimiter = ',')

    #Read the header row first
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate Total Number of Months, Net Amount of Profit/Loss, and Set Variables for Rows
    first_row = int(row[1])
    total_months += 1
    net_total += 1
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #Read each row of Data after the header
    for row in csvreader:

        #Calculate Total Number of Months 
        total_months += 1

        #Calculate Net Amount of Profit/Loss Over the Entire Data Period
        net_total += int(row[1])

        #Calculate Change from month to month
        revenue_change = int(row[1]) - first_row
        monthly_change.append(revenue_change)
        first_row = int(row[1])
        month_count.append(row[1])

        #Calculate the Greatest Increase in Profits and Month
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1]) 
            greatest_increase_month = row[0]

        #Calculate the Greatest Decrease in Profits and Month
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int (row[1])
            greatest_decrease_month = row[0]

    #Calculate the Average Change 
    average_change = sum(monthly_change)/len(monthly_change)
    round(int(average_change),2)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print
print(f"Analysis")
print(f"----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits;, {greatest_decrease_month}, (${lowest})")

#Set output file
output_file = csvpath = os.path.join ('/' 'Users', 'rebeccatast', 'Desktop', 'Python-Challenge','PyBank', 'Analysis', 'budget_data.txt')


#Open File Using Write Mode 
with open (output_file, 'w',) as txtfile:

    #Write New Data in Output File
    txtfile.write(f"Analysis\n")
    txtfile.write(f"----------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits;, {greatest_decrease_month}, (${lowest})\n")




    