#Exercise 5: Minimalist Email Client

mbox = input("Enter File Name: ")
count = 0

try:
    fhand = open(mbox)
except:
    print("File cannot be processed!")
    exit()

for line in fhand:
    if not line.startswith("From "):
        continue
    count = count + 1
    mail = line.split()
    print(mail[1])

print("There are ",count," lines in the file that start with the word From")
