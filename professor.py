from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def print_name(self):
        print(f"Professor first name is {self.first_name}")

    def subject_list(self):
        print(f"List of subjects:")
        for subject in self.lectures:
            print(f"- {subject.name}")

    def add_subject(self, new_subject):
        self.lectures.append(new_subject)

    def remove_subject(self, lecture):
        self.lectures.pop(lecture)
