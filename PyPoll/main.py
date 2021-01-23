#import os module, csv file and direct to pathway
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#read csv file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    total_votes = 0
    candidates_dict = {}
    
    print("Election Results")
    print("-------------------------")

    print("Election Results", file=open("analysis/output.txt","w"))
    print("-------------------------", file=open("analysis/output.txt","a"))
    
    for row in csvreader:
        total_votes +=1
        candidate = row[2]
        if candidate not in candidates_dict:
            candidates_dict[candidate]=0
        candidates_dict[candidate]+=1
    
    print(f'Total Votes: {total_votes}')
    print("-------------------------")

    print(f'Total Votes: {total_votes}', file=open("analysis/output.txt","a"))
    print("-------------------------", file=open("analysis/output.txt","a"))

    winner_ratio = 0    
    for i in candidates_dict:
        candidate_ratio=candidates_dict[i]/total_votes
        if candidate_ratio > winner_ratio:
            winner_ratio = candidate_ratio
            winner = i

        candidate_percent = "{:.3%}".format(candidate_ratio)

        print(f'{i}: {candidate_percent} {candidates_dict[i]}')
        print(f'{i}: {candidate_percent} {candidates_dict[i]}', file=open("analysis/output.txt","a"))
    
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

    print("-------------------------", file=open("analysis/output.txt","a"))
    print(f'Winner: {winner}', file=open("analysis/output.txt","a"))
    print("-------------------------", file=open("analysis/output.txt","a"))