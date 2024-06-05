# Step 1: Create a program

# Step 2: Take 5 numbers from the users
numbers = []
for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

# Step 3: Add 1-2 duplicates
numbers.extend([numbers[0], numbers[-1]])  # Adding first and last number as duplicates

# Step 4: Print the non-duplicate numbers
non_duplicates = list(set(numbers))
print("Non-duplicate numbers are:", non_duplicates)
