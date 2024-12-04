class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        #Display the employee's details.
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")

    def update_salary(self, new_salary):
        """Update the employee's salary."""
        self.salary = new_salary
        print(f"Salary updated to ${self.salary:,.2f} for {self.name}.")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        #Add an employee to the department.
        self.employees.append(employee)
        print(f"{employee.name} has been added to the {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        #Calculate and display the total salary expenditure for the department.
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for the {self.department_name} department: ${total_salary:,.2f}")

    def display_all_employees(self):
        #Display all employees in the department.
        if self.employees:
            print(f"Employees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department.")


# Function to interactively add employees and display total expenditure
def interactive_session():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nOptions: ")
        print("1. Add a new employee")
        print("2. Update employee salary")
        print("3. Display all employees")
        print("4. Calculate and display total salary expenditure")
        print("5. Exit")
        
        option = input("Select an option (1/2/3/4/5): ")

        if option == '1':
            # Add a new employee
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)
        
        elif option == '2':
            # Update employee salary
            employee_id = input("Enter employee ID to update salary: ")
            new_salary = float(input("Enter the new salary: "))
            # Find the employee and update salary
            found = False
            for employee in department.employees:
                if employee.employee_id == employee_id:
                    employee.update_salary(new_salary)
                    found = True
                    break
            if not found:
                print(f"Employee with ID {employee_id} not found.")
        
        elif option == '3':
            # Display all employees
            department.display_all_employees()
        
        elif option == '4':
            # Calculate and display total salary expenditure
            department.calculate_total_salary_expenditure()
        
        elif option == '5':
            print("Exiting the session.")
            break
        
        else:
            print("Invalid option. Please try again.")