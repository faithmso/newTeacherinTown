import itertools
from roster import student_roster
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.count = 0
    return self.count

  def __next__(self):
    self.count += 1
    

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students