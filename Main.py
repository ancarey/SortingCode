import random
from Sorting import Sorting
randomNumbers = []

print("\n<------------------------------------------------------------------------->")
print("                     WELCOME TO ELLIS'S SORTING STATION                      ")
print("<------------------------------------------------------------------------->\n")

arrayRange = int(input("How many numbers would you like to be sorted? "))
for i in range(arrayRange):
    randomNumbers.append((random.randint(1, 101)))

print("\nUnsorted Array: ", randomNumbers,"\n")


sort = Sorting(randomNumbers)
randomNumbers = sort.bubbleSort()

print("\nSorted Array:", randomNumbers)

print("\n<------------------------------------------------------------------------->")
print("                     ELLIS'S SORTING STATION SAYS GOODBYE                      ")
print("<------------------------------------------------------------------------->\n")
