class Lecture:
    def __init__(self, name, max_number, duration, professor_list):
        self.name = name
        self.max_number = max_number
        self.duration = duration
        self.professor_list = professor_list

    def print_name_duration(self):
        print(f"{self.name} -- {self.duration} minutes")

    def add_professor(self, new_professor):
        self.professor_list.append(new_professor)