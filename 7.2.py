class student:
    def __init__ (self, name, marks):
        self.name=name
        self.marks=marks
        def print_student_info(student):
            print(f"name:{self.name},marks:{self.marks}")
s1 = student("tillu", 92)
s1.print_info()
    
