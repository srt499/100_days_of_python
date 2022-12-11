import random
import pandas
# Take a list of numbers and put it in a new list adding 1 to each number
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append((add_1))

# List Comprehension version of the above
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

# List Comprehension Template
# new_list = [new_item for item in old_list]

# Conditional List Comprehension Template
# new_list = [new_item for item in list if test]

# Dictionary Comprehension Template
# new_dict = {new_key:new_value for (key,value) in dict.items()} <-- this is from dictionary to dictionary
# new_dict = {new_key: new_value for item in list} <-- this is from list to dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
name = "Brian"
letters = [letter for letter in name]
print(letters)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names)

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key, value)

# How to iterate/loop through a Pandas DataFrame
student_df = pandas.DataFrame(student_dict)
print(student_df)

#Loop through rows of a data frame in pandas
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
