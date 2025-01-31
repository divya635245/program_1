#Loop through a List
#Task: iterate through a list and perform calculations.

# Define the list of numbers
numbers = [10, 20, 30, 40, 50]

# Loop through the list and print each number multiplied by 2
for num in numbers:
    print(num * 2)

# Calculate and print the sum of all numbers in the list
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)



#List of comprehension
#Task: create a filterd list using list cpmprehension.

# Given list of numbers
numbers = [5, 12, 17, 24, 35]

# Create a new list containing only numbers greater than 15
filtered_numbers = [num for num in numbers if num > 15]

# Square all the numbers in the filtered list using list comprehension
squared_numbers = [num ** 2 for num in filtered_numbers]

# Print both lists
print("Filtered numbers:", filtered_numbers)
print("Squared numbers:", squared_numbers)



#The Syntax
#Task: create and manipulate lists.

# Create a list of strings
fruits = ["apple", "banana", "cherry", "date"]

# Add "orange" to the list
fruits.append("orange")

# Insert "grape" at index 2
fruits.insert(2, "grape")

# Remove "date" from the list
fruits.remove("date")

# Print the final list
print(fruits)


#Sort List
#Task: sort number in a list.

# Given list of numbers
numbers = [42, 12, 89, 33, 7]

# Sort in ascending order
numbers.sort()
print("Ascending order:", numbers)

# Sort in descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)

# Reverse the list again
numbers.reverse()
print("Reversed list:", numbers)




#Sort list (Alphanumerically)
#Task: Sort a list of string.

#Create the list of names:
names = ["Emma", "Olivia", "Liam", "Noah", "Sophia"]

# Sort alphabetically
names_sorted = sorted(names)
print("Alphabetically sorted:", names_sorted)

# Sort in reverse alphabetical order
names_sorted_reverse = sorted(names, reverse=True)
print("Reverse alphabetically sorted:", names_sorted_reverse)

# Add "James" to the list
names.append("James")

# Sort again after adding "James"
names_sorted_with_james = sorted(names)
print("Alphabetically sorted after adding 'James':", names_sorted_with_james)



#Descanding order
#Task: sort numbers and string in descanding order

#Give list of numbers
numbers = [50, 10, 70, 30, 90]

#sort in descanding order
numbers.sort(reverse=True)
print("Descanding order:" , numbers)

#Give a list of string
Animals = ["dogs", "cat", "zebra", "elephant", "ant"]

#sort in reverse alphabetical order
numbers.sort(reverse=True)



