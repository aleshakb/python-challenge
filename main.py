import os
# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
totalmonths = 0
totalrevenue = 0
revenue = []
previousrevenue = 0
month_of_change = []
revenuechange = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        totalmonths = totalmonths + 1
        totalrevenue = totalrevenue + int(row[1])

        revenuechange = int(row[1])- previousrevenue
        #print(revenuechange)
        previousrevenue = int(row[1])
       #print(int(row[1]))
        revenue_change_list = revenue_change_list + [revenuechange]
        #print(revenue_change_list)
        month_of_change = [month_of_change] + [row[0]]

        if revenuechange>greatest_increase[1]:
                    greatest_increase[1]= revenuechange
                    greatest_increase[0] = row[0]

        if revenuechange<greatest_decrease[1]:
                    greatest_decrease[1]= revenuechange
                    greatest_decrease[0] = row[0]
        
    print(totalmonths)
    print (totalrevenue)
    print(sum(revenue_change_list[1:])/len(revenue_change_list[1:]))   
    print(greatest_increase)
    print(greatest_decrease)
