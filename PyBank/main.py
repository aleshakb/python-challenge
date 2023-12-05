#import modules
import os
import csv
import pandas

#set path for file
budget_data_csv = os.path.join('Resources','budget_data.csv')
# C:\Users\Student6\Desktop\Homework\python-challenge\PyBank\Resources

#set the output of the text file
text_path = "new_output.txt"

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open(budget_data_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)
    print(csvreader)
    print(type(csvreader))

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months += 1

        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = int(row["Profit/Losses"]) - previous_revenue #change from float to int
        previous_revenue = int(row["Profit/Losses"]) #change from float to int
        revenue_change_list.append(revenue_change)
        month_of_change.append(row["Date"])      

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']

    #revenue_change_list = revenue_change_list.append(revenue_change_list)
    revenue_average = sum(revenue_change_list) / (total_months - 1)
    print (revenue_change_list)
    print (revenue_average)

#write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
