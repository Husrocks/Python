#Module 1: Variables and Basic Data Types
#its in variable file


#Module 2: Control Flow
#Control flow allows your program to make decisions and repeat actions.In ML and AI, this is used constantly—for example, to stop training a model once it reaches a certain accuracy or to loop through thousands of images in a dataset.



#Student Performance Prediction
Math_score = 45

if Math_score >= 80:
    print ("Excellent Performance")
elif Math_score >= 60:
    print ("Good Performance")
elif Math_score >= 40:
    print("average Performance")
else:
    print("Needs Academic Support")

#Fraud Detection
Transaction_amount = 100
if Transaction_amount >= 10000:
    print ("Flag for Fraud Investigation")
else:
    print("transaction Approved")

male = int(input("Enter number of males"))
Female = int(input("Enter number of Females"))
if male >=100:
    print("Males are more than females")
    if male >=100 and Female <100:
        print("nested if succeed")
    else:
        print("nested if is not succed ")
else:
    print("else statemaent ")

epoches=int(input("cycle "))
if epoches <= 200:
    print("its under trainin")
elif epoches >200:
    print("traind")
else:
    print ("no found")    
    
fruit=str(input("add colour"))
if fruit =='pink':
  print("husnain")
else:
  print("salar")  

samples = int(input("Enter number of samples: "))
print (samples +1)

sample_count = input("Enter a number: ")

try: 
    sample_count = int (sample_count)
    print(f"you entered {sample_count} samples.")
except ValueError:
    print("enter a number a whole number such as 20")



#Loops

#Processing Student Scores
#Imagine you have 1,000 student records. You can use a loop to process each student's score.

scores= [85,73,89,21]
for score in scores:
    if score >= 40:
        print (f"Score:{score} , Passed")
    else:
        print (f"Score:{score},Failed")
# Using a while loop to simulate a training countdown
countdown = 3
while countdown > 0:
    print(f"Training starts in {countdown}...")
    countdown -= 1  # Decrement by 1
print("Training started!")

#Calculating Prediction Errors
actual_scores = [43 , 89 , 87 , 43]
predicted_scores = [43,65,23,87]
for i in range(len(actual_scores)):
    error = actual_scores[i] - predicted_scores[i]
    print (f"The actual score is {actual_scores[i]}, the predicted score is {predicted_scores[i]} and the prediction error is {error}.")

#another approach to calculate prediction errors
# zip function is used to iterate multiple lists.
for actual, predicted in zip(actual_scores, predicted_scores):
    error = actual - predicted
    print (f"The actual score is {actual}, the predicted score is {predicted} and the prediction error is {error}.")


#Model Training Simulation

epoch = 1
max_epoch = 6
while epoch<= max_epoch:
    print("Training Epoch:", epoch)
    epoch +=1

max_epoch = 6
for epoch in range(1,max_epoch+1):
    print ("Training Epoch:", epoch)


#house price classification
house = [{"location":"Lahore","price":100000},{"location":"Karachi","price":200000},{"location":"Islamabad","price":300000}]
for h in house:
    price = h["price"]
    if price >= 200000:
        status = "Expensive"
    elif price >= 100000:
        status = "Moderate"
    else:
        status = "Affordable"
    print (f"The house in {h['location']} is {status} with a price of {price}.")

attempt = 0

while attempt < 3:
    print("Training attempt", attempt + 1)
    attempt +=1

#risk classification based on scores
    scores = [90, 25, 45, 32, 78, 55, 20, 88]
    high_risk_count = 0
    moderate_risk_count = 0
    low_risk_count = 0
    for sc in scores:
        if sc<40:
            print(f"SCORE: {sc} High Risk")
            high_risk_count += 1
        elif sc<59 and sc>=40:
            print(f"SCORE: {sc} Moderate Risk")
            moderate_risk_count += 1
        else:
            print(f"SCORE: {sc} Low Risk")
            low_risk_count += 1
    print (f"there are {len(scores)} students in the class")
    print (f"High Risk: {high_risk_count}, Moderate Risk: {moderate_risk_count}, Low Risk: {low_risk_count}")
            


#the accuracy gate 
model_accuracy = float(input("Enter accuracy: "))
if model_accuracy >= 0.95:
    print("Deploy to production")
elif model_accuracy >= 0.80 and model_accuracy<= 0.94:
    print("Requires more training")
elif model_accuracy < 0.80:
    print("Failed")
#the data processor
for number in range(1,11):
    square = number**2
    print(square)
#optimizer
loss = 0.5
while loss > 0.1 :
    loss -= 0.1 
    # Round to avoid floating-point precision artifacts (e.g., 0.30000000000000004)
    loss = round(loss, 1)
    print(f"the loss is",loss)


