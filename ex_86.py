#Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

list = []

while True:
    val = input("Enter a number: ")

    if val == 'done':
        break
    try:
        flVal = float(val)
    except:
        print("Please enter a number, or enter done if you are finished")
        continue
        
    list.append(flVal)

valMax = max(list)
valMin = min(list)

print("Maximum: ",valMax)
print("Minimum: ",valMin)
