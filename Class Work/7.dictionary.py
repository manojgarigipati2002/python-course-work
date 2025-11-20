# -------------------------------------------------------
#               PYTHON DICTIONARIES – FULL DEMO
# -------------------------------------------------------

# 1. Creating Dictionaries
print("1. DICTIONARY CREATION")

student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}

empty_dict = {}
another_dict = dict(name="Bob", age=25)

print("Student Dictionary:", student)
print("Empty Dictionary:", empty_dict)
print("Another Dictionary:", another_dict)
print("-" * 50)


# 2. Accessing Values
print("2. ACCESSING VALUES")

print("Name:", student["name"])                   # direct access
print("Age using get():", student.get("age"))     # safe access

# get() with default value
print("City (default):", student.get("city", "Not Available"))

print("-" * 50)


# 3. Adding & Updating Items
print("3. ADDING & UPDATING ITEMS")

student["age"] = 22             # update
student["city"] = "New York"    # add new
print("After update:", student)

print("-" * 50)


# 4. Removing Items
print("4. REMOVING ITEMS")

# pop()
removed_age = student.pop("age")
print("Removed age using pop():", removed_age)

# del
del student["course"]
print("After deleting 'course':", student)

# popitem()
last_item = student.popitem()
print("Last removed item:", last_item)
print("After popitem():", student)

# clear()
student.clear()
print("After clear():", student)

print("-" * 50)


# Re-create dictionary for next sections
student = {
    "name": "Alice",
    "age": 21,
    "course": "CS"
}


# 5. Dictionary Methods
print("5. DICTIONARY METHODS")

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# update()
student.update({"city": "London"})
print("After update({'city': 'London'}):", student)

# setdefault()
student.setdefault("phone", "Not Provided")
print("After setdefault():", student)

print("-" * 50)


# 6. Built-in Functions
print("6. BUILT-IN FUNCTIONS")

scores = {1: 50, 3: 90, 2: 70}

print("Length:", len(scores))
print("Max key:", max(scores))
print("Min key:", min(scores))
print("Sorted keys:", sorted(scores))

print("-" * 50)


# 7. Nested Dictionaries
print("7. NESTED DICTIONARY")

students = {
    "Alice": {"age": 21, "course": "CS"},
    "Bob": {"age": 22, "course": "Math"}
}

print("Alice's course:", students["Alice"]["course"])
print("Bob's age:", students["Bob"]["age"])

print("-" * 50)


# 8. Dictionary Comprehension
print("8. DICTIONARY COMPREHENSION")

squares = {x: x*x for x in range(1, 6)}
print("Squares:", squares)

print("-" * 50)


# 9. Real-Time Problem 1: Word Frequency
print("9. REAL-TIME PROBLEM – WORD FREQUENCY")

sentence = "hello world hello python"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)

print("-" * 50)


# 10. Real-Time Problem 2: Highest Marks
print("10. REAL-TIME PROBLEM – HIGHEST MARKS")

marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88
}

top_student = max(marks, key=marks.get)
print("Student with highest marks:", top_student)

print("-" * 50)

print("PROGRAM COMPLETED SUCCESSFULLY!")