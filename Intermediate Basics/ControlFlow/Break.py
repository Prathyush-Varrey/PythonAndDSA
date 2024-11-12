''' 
You can use break and continue to control loops:

break exits the loop immediately.
continue skips the current iteration and moves to the next.
'''


for i in range(10):
    if i == 5:
        break  # Stops the loop when i is 5
    if i % 2 == 0:
        continue  # Skips even numbers
    print(i)
