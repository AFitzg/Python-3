import os
import csv

#path for files
election_data_csv = os.path.join('Resources','election_data.csv')
analysispolls = os.path.join('analysis','analysispybank.txt')

#election statistics 
#you need total votes, list of candidates that received votes
#tuples and lists will be helpful
#Number of votes per candidate, percentage of votes won per candidate
#winner
totalvotes = 0

#list of candidates
candidates = []
individual_candidate_votes = []
#----------------------------

#movement of files & handling
with open (election_data_csv, "r") as csvreader:
    reader = csv.reader(csvreader,delimiter = ",")
    Header = next(reader)
    firstrow = next(reader)
    totalvotes = totalvotes + 1


    for row in reader:
        totalvotes = totalvotes + 1
        individual_candidate_name = (row[2])
        #calc for total votes in file & allows you to read the candidate names from column 3 via ([])

        if  individual_candidate_name in candidates:
            candidate_tag = candidates.index(individual_candidate_name)
            individual_candidate_votes[candidate_tag] = individual_candidate_votes[candidate_tag] + 1
        #looking at individual candidate in list of candidates,if a candidate name comes up when you're going through your rows then tag it
        #.index returns the position at the first occurence of the specified value
        #for each time your tagged candidate is found, add to their votes 1 time and add to their total votes
        else:
            candidates.append(individual_candidate_name)
            individual_candidate_votes.append(1)
        #looking at individual candidate in list of candidates, if that candidate's name doesn't come up when you're going through your rows then add the candidates name to your candidate list
        #list.append() adds the element() to your list
        #then add a vote (element) to your individual candidate votes(list)
    
#need to loop through again

percent_of_all_votes = []
winner_votes = individual_candidate_votes[3]
winner = 0

for candidate_stats in range(len(candidates)):
        #to access each item in a for loop by index use range() and len()
        #to get your candidate info or stats tied to the candidates in your list of candidates
        candidate_vote_percentage = round((individual_candidate_votes[candidate_stats]/totalvotes)*100)
        percent_of_all_votes.append(candidate_vote_percentage)
        #caluclate how to get the percentage of votes for each candidate
        #Add your candidate's vote percentage to their percent of all votes each time you loop through
        if individual_candidate_votes[candidate_stats] > winner_votes:
            winner_votes = individual_candidate_votes[candidate_stats]
candidate_stats = 0 + 1
Winning_candidate = candidates[candidate_stats]
    #your winning candidate is equal to the candidate stats with winning votes + 1 or it gives you the first person in your list

#final output
output= "Election Results\n"
output+= "-----------------------------------------\n"
output+= f"Total Votes: {totalvotes}\n"
output+="-----------------------------------------\n"
for candidate_stats in range(len(candidates)):
    output+=f"{candidates[candidate_stats]}: {percent_of_all_votes[candidate_stats]}.000%, ({(individual_candidate_votes[candidate_stats])}) \n"
output+="-----------------------------------------\n"
output+=f"Winner: {Winning_candidate}\n"
output+="-----------------------------------------" 

print(output)

with open (analysispolls, "w") as txtfile:
    txtfile.write(output)