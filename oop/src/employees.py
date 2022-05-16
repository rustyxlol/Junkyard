"""
Simple OOPS demonstration
"""


class Employee:
    """
    Employee class
    """

    total_employees = 0
    bonus_salary = 10000

    def __init__(self, first_name, last_name, email_id, salary=40000):
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def from_string(cls, emp_string):
        """
        Alternative constructor

        :param emp_string: of the form firstname-lastname-emailid
        :return: Instance of Employee
        """
        first, last, email = emp_string.split('-')
        return cls(first, last, email)

    def get_employee(self):
        """
        Returns information of an instance
        """
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}"

    def apply_bonus(self):
        """
        Increments salary
        """
        self.salary += self.bonus_salary

    def __repr__(self):
        return f"Employee('{self.first_name}', \
                          '{self.last_name}',\
                          '{self.email_id}', \
                           {self.salary})"

    def __str__(self):
        return f"Employee({self.first_name} {self.last_name} - {self.email_id})"


class Developer(Employee):
    """
    Inheritance Demo 1
    """

    def __init__(self, first, last, email, salary, prog_lang):
        super().__init__(first, last, email, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    """
    Inheritance Demo 2

    :param Employee: _description_
    """

    def __init__(self, first, last, email, salary, developers=None):
        super().__init__(first, last, email, salary)
        if developers is None:
            self.developers = []
        else:
            self.developers = developers

    def add_developer(self, developer):
        """
        Adds a developer to a manager instance
        """
        if developer not in self.developers:
            self.developers.append(developer)

    def remove_developer(self, developer):
        """
        Removes a developer from a manager instance
        """
        if developer in self.developers:
            self.developers.remove(developer)

    def print_developers(self):
        """
        Prints all developers under a manager instance
        """
        for index, developer in enumerate(self.developers):
            print(index + 1, developer)


if __name__ == "__main__":
    corey = Employee.from_string('Corey-Schafer-cs@youtube.com')

    dev_1 = Developer('Rusty', 'Hawker', 'rhemail@pm.me', 5000000, 'Python')
    dev_2 = Developer('Dusty', 'Cawker', 'dcemail@pm.me', 5000000, 'C#')

    mgr_1 = Manager('Karen', 'Smith', 'kall@manager.com', 5000000)

    print(f"corey = {corey}")
    print(f"dev_1 = {dev_1}")
    print(f"dev_2 = {dev_2}")
    print(f"mgr_1 = {mgr_1}")

    mgr_1.add_developer(dev_1)

    print(f"Total employees = {Employee.total_employees}")

    mgr_1.print_developers()
