class Student:
  """
  Student class with name and grades attributes.
  """
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def __str__(self):
    """
    Defines how a Student object is printed.
    """
    grade_str = ", ".join(f"{subject}: {grade}" for subject, grade in self.grades.items())
    return f"Name: {self.name}\nGrades: {grade_str}\n"


class Classroom:
  """
  Classroom class manages a list of students and provides functionalities to add, display, and calculate averages.
  """
  def __init__(self):
    self.students = []

  def add_student(self, student):
    """
    Adds a student object to the classroom list.
    """
    self.students.append(student)

  def display_all_students(self):
    """
    Iterates over the student list and prints details of each student.
    """
    if not self.students:
      print("No students in the classroom yet.")
      return
    for student in self.students:
      print(student)
      print("-" * 20)

  def get_student_average(self, student_name):
    """
    Calculates and returns the average grade for a specific student.
    Returns None if the student is not found.
    """
    for student in self.students:
      if student.name == student_name:
        return sum(student.grades.values()) / len(student.grades)
    return None

  def get_class_average(self, subject):
    """
    Calculates and returns the average grade for a specific subject across all students.
    Returns None if the subject doesn't exist or no students have grades yet.
    """
    total_grade = 0
    student_count = 0
    for student in self.students:
      if subject in student.grades:
        total_grade += student.grades[subject]
        student_count += 1
    if student_count == 0:
      return None
    return total_grade / student_count


# Demonstration
classroom = Classroom()

# Add some students with grades
student1 = Student("Alice", {"Math": 85, "Science": 90, "English": 78})
student2 = Student("Bob", {"Math": 70, "Science": 82, "English": 95})
classroom.add_student(student1)
classroom.add_student(student2)

# Display all students
print("Students in Class:")
classroom.display_all_students()

# Get student average
alice_average = classroom.get_student_average("Alice")
if alice_average:
  print(f"\nAlice's average grade: {alice_average}")
else:
  print(f"\nStudent named Alice not found.")

# Get class average
math_average = classroom.get_class_average("Math")
if math_average:
  print(f"\nClass average for Math: {math_average}")
else:
  print(f"\nNo grades available for Math or no students in the class.")

