class Employee:

    total_employees = 0
    bonus_salary = 10000

    def __init__(self, first_name, last_name, employee_id, email_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.email_id = email_id
        self.salary = salary
        Employee.total_employees += 1

    def get_employee(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}"

    def apply_bonus(self):
        self.salary += self.bonus_salary

    def __repr__(self):
        return f"Employee({self.employee_id}, {self.email_id}, {self.first_name}, {self.last_name})"


if __name__ == "__main__":
    corey = Employee('Corey', 'Schafer', '420', 'cs@shafer.com', 40000)
    norey = Employee('Norey', 'Schafer', '420', 'ns@shafer.com', 40000)
    print(corey.get_employee())
    print(norey.get_employee())

    corey.apply_bonus()
    print(corey.get_employee())

    norey.bonus_salary = 12345
    norey.apply_bonus()
    print(norey.get_employee())

    print("Total employees: ", Employee.total_employees)
