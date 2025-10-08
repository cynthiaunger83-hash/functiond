"""
a tuple is:
Orderd (we access elements by index)
unchangeble (immutable)- we cannot add/remove or change values
allowes dups
faster than a lsit
"""
#tuples use ()
fruits = ("apple", "bannana", "drangon fruit", "apple")
print(fruits)
print(len(fruits))
print(fruits[1])

#use if values in tuple:
print("apple" in fruits) #true
print("orange" in fruits) #false

#counr items in fruit
print(fruits.count("apple"))#2

#find index of elemt 
print(fruits.index("bannana"))#1
#print(fruits.index("car"))#throes value error if elemenrt is nt valid

#loop through a tuple
index = 0 
while index < len(fruits):
    print(fruits[index])
    index += 1 


for fruit in fruits:
    print(fruit)


