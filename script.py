from itertools import chain, combinations
from roster import student_roster
from classroom_organizer import ClassroomOrganizer

iterator = iter(student_roster)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

organizer = ClassroomOrganizer()
for student_name in organizer:
  print(student_name)

table_combinations = organizer.get_table_combinations()

for i, combination in enumerate(table_combinations, start=1):
  print(f"Table {i}: {combination}")

math_students = organizer.get_subject_combinations('Math')
science_students = organizer.get_subject_combinations('Science')

print("Math combinations:")
print(math_students)
print("Science combinations:")
print(science_students)
print("After School Combinations:")

afterschool_list = list(chain(math_students, science_students))
print(afterschool_list)
afterschool_table = list(combinations(afterschool_list,4))
print("After School Tables:")
print(afterschool_table)