from Employees_Manager import *

class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeesManager()

    def print_menu(self):
        print("\nprogram options: ")
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Update salary given a name',
            '4) End the program'
        ]
        print('\n'.join(messages))
        msg = f'Enter your choice(from 1 to {len(messages)}): '
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.EmployeesManager.add_employee()
            elif choice == 2:
                self.EmployeesManager.list_employee()
            elif choice == 3:
                name = input("Enter employee name: \n")
                salary = input("Enter employee salary \n")
                self.EmployeesManager.update_salary_by_name(name, salary)
            else:
                break
a = FrontendManager()
a.run()