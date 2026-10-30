#Conditionals 
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


#Loops

#Processing Student Scores
#Imagine you have 1,000 student records. You can use a loop to process each student's score.

scores= [85,73,89,21]
for score in scores:
    if score >= 40:
        print (f"Score:{score} , Passed")
    else:
        print (f"Score:{score},Failed")

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
            

