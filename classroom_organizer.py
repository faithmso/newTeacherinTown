import itertools
from roster import student_roster
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
    self.index = 0
    self.student_roster = student_roster

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.sorted_names):
      raise StopIteration

    else:
      current_name = self.sorted_names[self.index]
      self.index += 1
      return current_name
    
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

  def get_table_combinations(self):
    all_combinations = []
    for combination in itertools.combinations(self.sorted_names, 2):
      all_combinations.append(combination)
    return all_combinations

  def get_subject_combinations(self, subject):
    subject_students = [student['name'] for student in self.student_roster if student['favorite_subject'] == subject]
    return subject_students
