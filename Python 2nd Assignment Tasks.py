"""
Author: UGOwealth
Age: 45
Height: 5.73 ft
Nationality: Nigerian
Description: This program contains multiple small tasks 
demonstrating Python basics with lists, tuples, dictionaries, 
sets, and list comprehension.
"""

# -------------------------
# Task 1: List and Sum
# -------------------------
print("=== Task 1: Create a list of integers and compute the sum ===")
numbers = input("Enter integers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]
print("List of integers:", numbers_list)
print("Sum of integers:", sum(numbers_list))
print("\n")

# -------------------------
# Task 2: Tuple of Books
# -------------------------
print("=== Task 2: Tuple of Favorite Books ===")
books = ("The Alchemist", "1984", "Atomic Habits", "The Richest Man in Babylon", "Python Crash Course")
for book in books:
    print(book)
print("\n")

# -------------------------
# Task 3: Dictionary for Person Info
# -------------------------
print("=== Task 3: Dictionary of a Person ===")
person = {}
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")
print("Person dictionary:", person)
print("\n")

# -------------------------
# Task 4: Sets and Common Elements
# -------------------------
print("=== Task 4: Common Elements in Two Sets ===")
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))
common_elements = set1 & set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Common Elements:", common_elements)
print("\n")

# -------------------------
# Task 5: List Comprehension (Odd-length words)
# -------------------------
print("=== Task 5: Words with Odd Number of Characters ===")
words = ["Python", "Code", "UGOwealth", "Nigeria", "Data", "Science"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Original words:", words)
print("Words with odd number of characters:", odd_length_words)
