"""
sets are slo collections
they are not orderd - meaning they dont have  a fixed position - cant accses by index
you cannot changfe exsisting itemns, but you can add/remove
dose not allowe dups
"""

trees = {"evergreen", " maple", "hickory", "oak" }
print(trees) #prints in a random order
#you cannot accses ellemts by index becuase it is unordered 
#print(trees[0]) #crash TypeError: "set" object is not subscribes

#add and remove from list
trees.add("palm") #note this is add not appens (that list use)
print(trees)
trees.remove("evergreen")
print(trees)
#sets do not allow dups
trees.add("palm")
print(trees) #palm was not added a second time

#quick trick to get clean list - if order does not matter
my_list = ["bennett", "bennett", "bennett", "draven", "levi", "liam"]
my_set = set(my_list)
my_list = list(my_set)
print(my_list)
