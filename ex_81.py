#Exercise 1: Write a function called chop that takes a list and modifies it,
#removing the first and last elements, and returns None.
#Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(t):
    del t[0]
    del t[-1]

def middle(x):
    new = x[1:-1]
    return new

li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]

out1 = chop(li1)
print(li1)
print(out1)

out2 = middle(li2)
print(li2)
print(out2)
