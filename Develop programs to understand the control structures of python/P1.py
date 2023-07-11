# Control Structure Example

# if-else statement
age = 25
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else statement
grade = 75
if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
else:
    print("You need to improve.")

# for loop
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum of numbers:", sum)

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# break and continue statements
for i in range(10):
    if i == 3:
        continue  # Skip the rest of the code in the loop and move to the next iteration
    if i == 7:
        break  # Exit the loop completely
    print(i)

# Pass Statement Example

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        pass  # Placeholder, no action needed for even numbers
    else:
        print(num)  # Print odd numbers

