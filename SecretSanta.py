# "Secret Santa" gift-assigner program


import random

# Here is a function to use later that checks to make sure nobody is
# assigned to buy a gift for themselves

def check(L1, L2, num):
	for i in range(num):
		if L1[i] == L2[i]:
			return True;
	return False;


# Main program

numPeople = int(input("How many people are playing? "))
players = []
receivers = []

print("Please enter their names: ")


# Get all of the players' names and add them to the list

for i in range(numPeople):
	players.append(input(""))


# Randomly assign gift receivers. If the "check" returns True, that means
# someone was assigned themselves (which is no fun!), in which case re-assign
# everyone and try again. Keep trying (looping) until everyone is giving to someone else.

myCheck = True
while(myCheck == True):
	receivers = random.sample(players, numPeople)
	myCheck = check(players, receivers, numPeople)


# Print results

print()
print("Secret Santa Gift Assignments...")
for k in range(numPeople):
	print(players[k], "will buy a gift for", receivers[k])
print()


# CHALLENGE ASSIGNMENT!
# This algorithm works but is inefficient because it completely starts from scratch
# in re-assigning everybody if even one person is assigned to give a gift to themselves.
# Can you design a better, more efficient algorithm?
# HINT - It's ok to create new lists  :-)

# CHALLENGE ASSIGNMENT!
# How can we avoid a Secret Santa "closed loop" where, for example, Player #1 buys a
# gift for Player #4, and vice versa - effectively closing the two of them off from
# everyone else?

# CHALLENGE ASSIGNMENT!
# Sometimes, it's no fun for certain people in a big Secret Santa exchange to buy gifts for
# each other (like spouses who will probably buy gifts for each other anyway).  Can you edit
# this program to account for such undesirable matchings?
# HINT - Read up on different Matching algorithms  :-)