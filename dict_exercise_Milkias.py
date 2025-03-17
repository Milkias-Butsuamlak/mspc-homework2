# %%
from rich import print

# %%
# ## Homework
#
# You are given a list of dictionaries, where each dictionary represents a student and contains their name and a list of grades. Write a Python function that:
#
#  * Iterates through the list of dictionaries.
# # * For each student, calculates their average grade.
# # * It sorts the grade.
# # * Adds a new key to the dictionary named 'average' that stores their average grade...
# # * Returns a list of dictionaries with the students' names and their average grades.
# #
# # Input
# # ```
# # students = [
# #     {'name': 'Alice', 'grades': [90, 85, 92]},
# #     {'name': 'Bob', 'grades': [70, 88, 80]},
# #     {'name': 'Charlie', 'grades': [95, 93, 97]}
# # ]
# # ```
# # Output
# # ```
# # [
# #     {'name': 'Alice', 'grades': [85, 90, 92], 'average': 89.0},
# #     {'name': 'Bob', 'grades': [70, 80, 88], 'average': 79.33},
# #     {'name': 'Charlie', 'grades': [97, 95, 93], 'average': 95.0}
# # ]
# # ```
# #
#
#
#
#

# %%
students = [
{'name': 'Alice', 'grades': [90, 85, 92]},
{'name': 'Bob', 'grades': [70, 88, 80]},
{'name': 'Charlie', 'grades': [95, 93, 97]}
]
x=students[0]["grades"]
for student in students:
    avg=sum(student["grades"])/len(student["grades"])
    student["average"]=avg
    student["grades"].sort()
print(students)

