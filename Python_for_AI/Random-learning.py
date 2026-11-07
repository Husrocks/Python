number = [1,2,3,4,5,6,7,8,9,10]

for i in  range(len(number)):
   numbers = number[i]*number[i]
   print ("square",numbers)

#try except
secret = 7
guess = None

while guess != secret:
    guess = input("Guess the number: ")
    try:
        guess = int(guess)
        print("Correct!")
    except ValueError:
        print("whole number")

#continue 
scores = [0.8, 0.75, 0.95, 0.8]

for score in scores:
    if score < 0.7:
        continue  # skip low scores
    if score > 0.9:
        print("Found a high score:", score)
        break

#built in functions 
scores = [0.7, 0.82, 0.91]

print(len(scores))   # number of items
print(sum(scores))   # sum of numeric items
print(min(scores))   # smallest value
print(max(scores))   # largest value
print(sorted(scores))  # new sorted list

import math 
from statistics import mean
scores = [0.7, 0.82, 0.91, 0.3, 0.10]
print(mean(scores))
print(math.sqrt(16))