# Module 2: Control Flow
Control flow allows your program to make decisions and repeat actions. In ML and AI, this is used constantly—for example, to stop training a model once it reaches a certain accuracy or to loop through thousands of images in a dataset.

1. Conditional Statements (if, elif, else)
These allow you to execute code only if a specific condition is true.

if: The initial check.
elif (short for else if): Used to check multiple conditions if the first one is false.
else: The fallback if none of the above conditions are met.
2. Loops (for and while)

for loop: Used to iterate over a sequence (like a list or a range of numbers). This is the most common loop in AI for processing data.
while loop: Repeats as long as a condition remains true.
Here is an example combining these concepts. Imagine we are checking the accuracy of three different AI models:


# A list of model accuracies
accuracies = [0.75, 0.92, 0.88]

# Using a for loop to check each model
for acc in accuracies:
    if acc >= 0.90:
        print(f"Accuracy {acc}: Excellent model!")
    elif acc >= 0.80:
        print(f"Accuracy {acc}: Good model, but needs tuning.")
    else:
        print(f"Accuracy {acc}: Poor performance.")

# Using a while loop to simulate a training countdown
countdown = 3
while countdown > 0:
    print(f"Training starts in {countdown}...")
    countdown -= 1  # Decrement by 1
print("Training started!")

# Now it's your turn. Try to solve these scenarios:

1. The Accuracy Gate: Create a variable called model_accuracy. Write a program that prints "Deploy to Production" if accuracy is 0.95 or higher, "Requires More Training" if it is between 0.80 and 0.94, and "Failed" if it is below 0.80.
2. The Data Processor: Use a for loop and the range() function to print the square of every number from 1 to 10. (Example: 1, 4, 9...).
3. The Optimizer: Create a variable loss = 0.5. Use a while loop to simulate an optimizer reducing the loss. In each iteration of the loop, subtract 0.1 from the loss and print the current value. Stop the loop once the loss is less than or equal to 0.1.