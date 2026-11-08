# Neural Network Training Simulation
# Advanced Beginner
# Imagine you are training a neural network. After each epoch, the model produces a loss value.

# Your tasks:
# 1. Use a while or for loop to process the loss values.
# 2. Print the loss after each epoch.
# 3. If loss becomes less than or equal to 0.10, print "Training Completed!".
# 4. Stop the loop using break.
# 5. Count how many epochs were required to reach the target loss.

losses = [0.95, 0.72, 0.54, 0.38, 0.21, 0.09, 0.04]
epoch = 0
for i in range(len(losses)):
    print(f"Epoch {epoch} loss: {losses[i]}")
    epoch +=1

    if losses[i] <= 0.10:
        print("Training completed!")
        break
print(f"total epoches: {epoch}")

# siplimfy
# enumerate() gives you both the index and value without manually maintaining a counter.
for epoch, loss in enumerate(losses, start=1):
    print(f"Epoch {epoch}: Loss = {loss}")

    if loss <= 0.10:
        print("Training completed!")
        break