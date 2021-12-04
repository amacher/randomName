import random
  
# initializing list 
names = ['Jane', 'Sally', 'Tim', 'George', 'Phil', 'Ann']

#Creates dictionary from the name and assigns 0 to them
names_dictionary = dict.fromkeys(names, 0)
count = 0

#while loop to go to 100 get the random count
while count < 1001:
    name = random.choice(names)
    names_dictionary[name] += 1
    count +=1

#Add a tie breaker here
#check if 2 values the same and create a tie breaker
result = {}
for val in names_dictionary:
    if names_dictionary[val] in result:
        result[names_dictionary[val]].append(val)
    else:
        result[names_dictionary[val]] = [val]

#Go through the ties and put in order
for key in result:
    ties = list(result[key])
    
    #Checks if each number has more than one person
    if len(ties) > 1:
        nameNum = len(names)
        if len(names) < 100:
                divBy = 100
        else:
            divBy = 1000
        tieBreaker = random.sample(ties, len(ties))
        for tie in tieBreaker:
            indexPlace = tieBreaker.index(tie)
            names_dictionary[tie] += (nameNum-indexPlace)/divBy

#sort the list so they will go from highest number to smallest
sort_winners = sorted(names_dictionary.items(), key=lambda x: x[1], reverse=True)

#Print the list one line at a time
for i in sort_winners:
	print(i[0], i[1])

