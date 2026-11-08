#Module 3: Data Structures

#list

models = ["Linear Regression", "Random Forest", "Neural Network"]
for number, model in enumerate(models, start=1):
    print(f"Model no {number}: {model}")

models[0] = "XGBoost"

print(models)


predictions = [5, 4, 3 , 6, 8, 10, 6]

# Add another model prediction
predictions.append(2)
predictions.append(1)
print(predictions)
predictions.remove(3)
print(predictions)
predictions.pop(2)

predictions.sort()
print(predictions)
predictions.reverse()
print(predictions)
print(len(predictions))

#slicing

print(predictions[0:3])
