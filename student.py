from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def lectures_list(self):
        print(f"Attended Lectures:")
        for lecture in self.lectures:
            print(f"- {lecture.name}")

    def add_lectures(self,new_lecture):
        self.lectures.append(new_lecture)

    def remove_lecture(self, lectures):
        self.lectures.pop(lectures)