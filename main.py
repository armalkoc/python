from lecture import Lecture
from professor import Professor
from person import Person
from student import Student

cs_lecture = Lecture("Computer science", 15, 45, [])
python_basics_lecture = Lecture("Python programming basics", 25, 90, [])
python_advanced_lecture = Lecture("Python advanced", 10, 90, [])
algorithms_lecture = Lecture("Algorithms and data sturctures", 30, 120, [])

new_professor = Professor("Maria", "Smith", 34, [cs_lecture, python_basics_lecture])
new_professor.print_name()
new_professor.add_subject(python_advanced_lecture)
new_professor.subject_list()

cs_lecture.add_professor(new_professor)
python_basics_lecture.add_professor(new_professor)
python_advanced_lecture.add_professor(new_professor)

print("------------------------------")

new_student = Student("David", "Green", 25, [algorithms_lecture])
new_student.print_name()
new_student.add_lectures(python_basics_lecture)
new_student.lectures_list()

print("------------------------------")

cs_lecture.print_name_duration()
python_basics_lecture.print_name_duration()
