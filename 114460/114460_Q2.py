class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        #Add an assignment and its grade to the student's record.
        self.assignments[assignment_name] = grade

    def display_grades(self):
        #Display the student's grades for each assignment.
        if self.assignments:
            print(f"Grades for {self.name} (ID: {self.student_id}):")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print(f"{self.name} has no assignments yet.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        #Add a student to the course.
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        #Assign a grade to a student for a specific assignment.
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Grade '{grade}' has been assigned to {student.name} for {assignment_name}.")
                return
        print(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        #Display all students and their grades.
        print(f"Students in {self.course_name} course:")
        for student in self.students:
            student.display_grades()


# Function to interactively add students and assign grades
def interactive_session():
    # Creating an instructor
    instructor_name = input("Enter the instructor's name: ")
    course_name = input("Enter the course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\nOptions: ")
        print("1. Add a new student")
        print("2. Assign a grade to a student")
        print("3. Display all students and their grades")
        print("4. Exit")
        
        option = input("Select an option (1/2/3/4): ")

        if option == '1':
            student_name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(student_name, student_id)
            instructor.add_student(student)
            print(f"Student {student_name} added to the course.")
        
        elif option == '2':
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)
        
        elif option == '3':
            instructor.display_all_students()
        
        elif option == '4':
            print("Exiting the session.")
            break
        
        else:
            print("Invalid option. Please try again.")
