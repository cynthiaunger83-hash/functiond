name = "joey" # stores a single value in a variable
print(name[0]) # can also get specidic characters in a string
 
age = 15
# a collection is going to allow us to store multiple values until one name
 
# a list - use []
# lists can be changed, can have duplicates, have positions (ordered)
games = ["dead space", "hollow knight", "eldenring", "oneshot"]
 
print(games)
# accessing items in the list
# single item:
print(games[1]) # lists are 0 indexed - the first element is index 0
# subset of the list:
print(games[0:2])
# you can also use the step function:
print(games[0:4:2])
# this is sthe same as:
print(games[::2])
 
# you can still crash
# IndexError: list index out of range
#print(games[4])
 
# you can know how long a list is
print(len(games))
# get the last element:
print(games[-1]) # python way
print(games[len(games)-1]) # common in other languages
 
# looping through a list
for game in games:
    print(game)
 
# find available methods
print(dir(games))
# print help docs
#print(help(list))
 
games.reverse()
print(games)
games.sort(reverse=True)
print(games)
 
# see if the item is in the list
print(f"is eldenring in our list: {"eldenring" in games}")
print(f"is mario in our list: {"mario" in games}")
 
# change an element in the list:
games[0] = "mario"
print(games)
 
elden_index = games.index("eldenring")
games[elden_index] = "ultrakill"
print(games)
 
# empty a list:
games.clear()
print(games)
 
# add element to the end of a list:
games.append("fortnite")
print(games)
# insert an element into the list:
games.insert(1, "donkey kong")
print(games)
# remove element from list:
games.remove("hollow knight")
print(games)
 
# for the rest of class:
# write a program that will continously ask the user for their favorite foods.
# take the input and add it to a list.
# when the user types Q, print the list.
 