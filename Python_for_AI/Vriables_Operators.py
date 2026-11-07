#variables
item = "Python"
topics = "variables"
print (f"I am learning {topics} in {item}.")
name = "Hussnain"
age = 20
is_learning_Python = True
print(f"My name is {name}, I am {age} years old and it is {is_learning_Python} that I am learning Python.")

hours_per_day = 2.5
days_per_week = 7
total_study_hours = hours_per_day * days_per_week
print(f"I study for {total_study_hours} hours per week.")


movie_title = "Inception"
release_year = 2010
IMDB_rating = 8.8   
has_won_oscar = True

print(f"{name} is watching the movie {movie_title} which was released in {release_year} and has an IMDB rating of {IMDB_rating} and it is {has_won_oscar} that it has won an Oscar.")

x = 10
y = 3

print (f"The sum of {x} and {y} is {x + y}.")
print (f"The difference between {x} and {y} is {x - y}.")
print (f"The product of {x} and {y} is {x * y}.")
print (f"The quotient of {x} divided by {y} is {x / y}.")
print (f"The remainder of {x} divided by {y} is {x % y}.")

temp = 50
print("the type of temp is ", type(temp))  
print(type(temp))  # <class 'float'>


#use python function to convert it to String 
temp_str = str(temp)
print(f"The temperature is {temp_str} degrees.")

a = 7
b = 2

print(a + b)   # 9: addition
print(a - b)   # 5: subtraction
print(a * b)   # 14: multiplication
print(a / b)   # 3.5: division
print(a // b)  # 3: floor division
print(a % b)   # 1: remainder
print(a ** b)  # 49: exponentiation

A =  (int(input("Enter a number A: ")))
B= (int(input("Enter a number B: ")))
print (A+B)

#Comparisons produce a Boolean (True or False):
#Use == to compare values and = to assign a value.


score = 0.82

score > 0.8     # True
score == 0.82   # True
score != 0.5    # True
score <= 1.0    # True


score = 0.82
has_label = True

if score >= 0.8 and has_label:
    print("This result meets both conditions.")



