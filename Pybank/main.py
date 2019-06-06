#Modules
import os
import csv

#set path for file 
csvpath = os.path.join("Resources", "budget_data.csv")

#open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header 
    csv_header = next(csvreader)
    #print the header 
    print(csv_header)
    #set total months as 0
    total_months = 0
    #set net profit as 0
    net_profit = 0
    #set maximum profit as 0
    max_profit_change = 0 
    #set minimum profit as 0
    min_profit_change = 0
    #create an empty list for storing the second column of profit/losses
    Profit_Loss = []
    #set sum of profit loss change(initially) as 0
    delta_profit_total = 0
    #create an empty list to store date
    date_list = []

    

    #Read every row of the csv file
    for row in csvreader:
        #calculate total months
        total_months +=1

        #calculate net total profit/losses
        net_profit += float(row[1])

        #Add profit/loss values  to the empty profit loss list

        Profit_Loss.append(float(row[1]))
        #Add date to the empty date list
        date_list.append(row[0])


       #Run a for loop on every element of the list
    for i in range(1,len(Profit_Loss)):
       #calculate the difference between every consecutive value
        delta_profit = (Profit_Loss[i]-Profit_Loss[i-1])

        #find the maximum profit change    
        if delta_profit>max_profit_change:
            max_profit_change = delta_profit
            max_date = date_list[i]

        #find the minimum profit change
        if delta_profit<min_profit_change:
            min_profit_change = delta_profit
            min_date = date_list[i]
        #calculate the sum of profit loss change
        delta_profit_total += delta_profit 

    
    average_change = delta_profit_total/(total_months-1)



#print the results         
print(f'Total Months = {total_months}')
print(f'Total = ${net_profit}')
print(f'Average change =${average_change}')
print(f'Greatest increase in  profit:${max_profit_change}({max_date})')
print(f'Greatest decrease in profit:${min_profit_change}({min_date})')

#output text file
with open('outfile.txt', 'w') as outfile:
    outfile.write(f'Total Months = {total_months}')
    outfile.write(f'Total = ${net_profit}')              
    outfile.write(f'Average change =${average_change}')             
    outfile.write(f'Greatest increase in  profit:${max_profit_change}({max_date})')              
    outfile.write(f'Greatest decrease in profit:${min_profit_change}({min_date})' )

outfile.close()


    















    



















