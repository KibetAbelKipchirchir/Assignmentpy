# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position
my_list.insert(1, 15)  # Index 1 refers to the second position

# Step 4: Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from the list
my_list.pop()  # Removes the last element by default

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find the index of the value 30 in the list and print it
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")

# Optional: Print the final state of my_list to verify
print(f"The final list is: {my_list}")
