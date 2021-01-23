#import os module, csv file and direct to pathway
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#read csv file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #print(csv_header)
    
    #calculate total months
    total_months = 0
    total_profit_losses = 0
    last_month_profit_loss = 0
    greatest_profit = 0
    greatest_loss = 0

    changes_list=[]
    for row in csvreader:
        total_months +=1
        monthly_profit_losses = int(row[1])
        total_profit_losses += monthly_profit_losses
        if total_months!=1:
            monthly_change = monthly_profit_losses-last_month_profit_loss
            changes_list.append(monthly_change)
            if monthly_change>greatest_profit:
                greatest_profit = monthly_change
                greatest_profit_date = row[0]
            if monthly_change<greatest_loss:
                greatest_loss = monthly_change
                greatest_loss_date = row[0]
        last_month_profit_loss = monthly_profit_losses
    average_change = sum(changes_list)/len(changes_list)
    #printing to terminal
    print("Financial Analysis")
    print("-------------------------")
    print(f'{"Total months: " +str(total_months)}')
    print(f'{"Total: $" +str(total_profit_losses)}')
    print(f'{"Average Change: $" +str(round(average_change,2))}')
    print(f'{"Greatest Increase in Profits: "+str(greatest_profit_date)+ " ($"+str(greatest_profit) + ")"}')
    print(f'{"Greatest Decrease in Profits: "+str(greatest_loss_date)+ " ($"+str(greatest_loss) + ")"}')

    #printing to text file
    print("Financial Analysis", file=open("analysis/output.txt","w"))
    print("-------------------------",file=open("analysis/output.txt","a"))
    print(f'{"Total months: " +str(total_months)}', file=open("analysis/output.txt","a"))
    print(f'{"Total: $" +str(total_profit_losses)}', file=open("analysis/output.txt","a"))
    print(f'{"Average Change: $" +str(round(average_change,2))}', file=open("analysis/output.txt","a"))
    print(f'{"Greatest Increase in Profits: "+str(greatest_profit_date)+ " ($"+str(greatest_profit) + ")"}', file=open("analysis/output.txt","a"))
    print(f'{"Greatest Decrease in Profits: "+str(greatest_loss_date)+ " ($"+str(greatest_loss) + ")"}', file=open("analysis/output.txt","a"))
