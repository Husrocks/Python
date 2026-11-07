loss = 0.5
while loss > 0.1 :
    loss -= 0.1 
    # Round to avoid floating-point precision artifacts (e.g., 0.30000000000000004)
    loss = round(loss, 1)
    print(f"the loss is",loss)
