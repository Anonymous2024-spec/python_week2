# Task 1: Create a list of integers from user input and compute their sum.
# We'll ask the user to input numbers separated by spaces.
numbers_input = input("Task 1 - Enter integers separated by spaces: ")
# Convert the input into a list of integers.
numbers_list = [int(num) for num in numbers_input.split()]
total = sum(numbers_list)
print("The sum of the numbers is:", total)
print("-" * 50)

# Task 2: Create a tuple containing five favorite books and print each on a separate line.
# You can replace the book names with your own favorites.
favorite_books = (
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "Brave New World",
    "Fahrenheit 451"
)
print("Task 2 - Favorite Books:")
for book in favorite_books:
    print(book)
print("-" * 50)

# Task 3: Use a dictionary to store information about a person.
person_info = {}
person_info["name"] = input("Task 3 - Enter your name: ")
# Use int() to convert age input into an integer.
person_info["age"] = int(input("Enter your age: "))
person_info["favorite_color"] = input("Enter your favorite color: ")
print("Person Information:")
print(person_info)
print("-" * 50)

# Task 4: Create two sets of integers from user input and find the common elements.
set1_input = input("Task 4 - Enter integers for set 1 separated by spaces: ")
set2_input = input("Enter integers for set 2 separated by spaces: ")
# Convert inputs into sets of integers.
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
common_elements = set1.intersection(set2)
print("Common elements between both sets:", common_elements)
print("-" * 50)

# Task 5: Create a list of words and then use list comprehension to filter words with an odd number of characters.
# Here we use a predefined list; you can change these words if you like.
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print("Words with an odd number of characters:", odd_length_words)
