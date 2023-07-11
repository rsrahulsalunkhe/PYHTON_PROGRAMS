# Data Structures Example

# List
fruits = ["apple", "banana", "cherry", "durian"]
print("Fruits List:", fruits)

# Accessing list elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying list elements
fruits[1] = "mango"
print("Modified Fruits List:", fruits)

# Dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
print("\nPerson Dictionary:", person)

# Accessing dictionary elements
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Modifying dictionary elements
person["age"] = 35
person["country"] = "USA"
print("Modified Person Dictionary:", person)

# Tuple
coordinates = (10, 20)
print("\nCoordinates Tuple:", coordinates)

# Accessing tuple elements
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])

# Tuples are immutable, cannot be modified
# coordinates[0] = 15  # This will result in an error

