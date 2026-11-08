# ML Model Performance Evaluation
# Intermediate
# You trained an ML model and obtained these accuracy scores across 5 experiments.

# Your tasks:
# 1. Use a loop to iterate through all accuracy scores.
# 2. If accuracy is greater than or equal to 0.90, print "Excellent Model".
# 3. If accuracy is between 0.75 and 0.89, print "Good Model".
# 4. Otherwise, print "Needs Improvement".
# 5. Count how many models achieved excellent accuracy.
# 6. Calculate the average accuracy.

accuracies = [0.85, 0.92, 0.67, 0.95, 0.73]
excellent_models = 0
for i in range(len(accuracies)):
    if accuracies[i ]>= 0.90:
        print("Excellent Model")
        excellent_models += 1 
    elif accuracies[i] > 0.75 and accuracies[i] <0.89 :
        print("Good model")
    else:
        print("Needs Improvement")

average = sum(accuracies)/ len(accuracies) * 100
        
print(f"this is the avrage accuracy: {average : .1f}%")
print(f"The excellent models are {excellent_models}")


#another approch

accuracies = [0.85, 0.92, 0.67, 0.95, 0.73]
excellent_models = 0
for index, accuracy in enumerate(accuracies):
    print(index, accuracy)
    if accuracy >= 0.90:
            print("Excellent Model")
            excellent_models += 1 
    elif accuracy > 0.75 and accuracy <0.89 :
            print("Good model")
    else:
            print("Needs Improvement")
    
average = sum(accuracies)/ len(accuracies) * 100
            
print(f"this is the avrage accuracy: {average : .1f}%")
print(f"The excellent models are {excellent_models}")
