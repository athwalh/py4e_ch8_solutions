#Exercise 4: Find all unique words in a file
#List all unique words, sorted in alphabetical order,that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

romeo = input("Enter File Name: ")
try:
    fhand = open(romeo)
except:
    print("File cannot be processed")
    exit()

s1 = ""

for line in fhand:
    s2 = line
    s1 = s1 + line

list = s1.split()
listUnique = []

for i in range(len(list)):
    if list[i] not in listUnique:
        listUnique.append(list[i])

listUnique.sort()

print(listUnique)
