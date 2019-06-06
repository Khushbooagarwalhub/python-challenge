

#Modules
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


 #skip the header
    csv_header = next(csvreader)
    print(csv_header)

    #create an empty list for storing unique candidates names 
    candidates_unique = []
    #create an empty list for storing  vote count of each candidate
    counts_list = []
    #create an empty list for storing vote percentage of each candidate
    count_list_percent =[]


    #set total vote as 0
    total_vote = 0
    
    # Read each row of the csv
    for row in csvreader:  
        #calculate total vote
        total_vote +=1
        #find unique names of candidates and store in the list
        if row[2] not in candidates_unique:
           candidates_unique.append(row[2])
        #initialize the counts list and count list percent 
           counts_list.append(0)
           count_list_percent.append(0)

        #run loop on each unique name 
        for i in range(0,len(candidates_unique)):

            # if statement for setting conditions 
            if row[2] == candidates_unique[i]:
            #calculate the total vote count for each candidate
               counts_list[i] = int(counts_list[i])+1
             #calculate the total vote percent for each candidate  
               count_list_percent[i] = (counts_list[i]/total_vote)*100
             # finding the maximum vote percent
               max_vote = max(count_list_percent)
             # check the index of the maximum vote to match with unique candidate name
               winner = candidates_unique[count_list_percent.index(max_vote)]



               

#print the results                

print(f'total_vote:{total_vote}')
print(candidates_unique)


print(f'{candidates_unique[0]}":{count_list_percent[0]} {counts_list[0]}')
print(f'{candidates_unique[1]}:{count_list_percent[1]} {counts_list[1]}')
print(f'{candidates_unique[2]}:{count_list_percent[2]} {counts_list[2]}')
print(f'{candidates_unique[3]}:{count_list_percent[3]} {counts_list[3]}')
print(f'Winner:{winner}')


#output text file

with open('outfile.txt', 'w') as outfile:
    outfile.write(f'total_vote:{total_vote}')
    outfile.write(f'{candidates_unique[0]}:{count_list_percent[0]} {counts_list[0]}')         
    outfile.write(f'{candidates_unique[1]}:{count_list_percent[1]} {counts_list[1]}')            
    outfile.write(f'{candidates_unique[2]}:{count_list_percent[2]} {counts_list[2]}')
    outfile.write(f'{candidates_unique[3]}:{count_list_percent[3]} {counts_list[3]}')
    outfile.write(f'Winner:{winner}')

    #outfile.close()



    
















      















