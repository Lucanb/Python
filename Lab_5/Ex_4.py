class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"{self.employee_id}: {self.name}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, {self.salary}, {self.department} Manager"

    def organize_team_meeting(self):
        return "Organizing a team meeting"

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()}, {self.salary}, Engineer specialized in {self.programming_language}"

    def write_code(self):
        return f"Writing code in {self.programming_language}"

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, territory):
        super().__init__(name, employee_id)
        self.salary = salary
        self.territory = territory

    def display_info(self):
        return f"{super().display_info()}, {self.salary}, Salesperson covering {self.territory}"

    def make_sales_pitch(self):
        return "Making a sales pitch"

manager = Manager(name="Ion Bat", employee_id="123", salary=80000, department="Marketing")
print(manager.display_info())
print(manager.organize_team_meeting())
engineer = Engineer(name="BEN DOVER", employee_id="456", salary=70000, programming_language="Python")
print(engineer.display_info())
print(engineer.write_code())
salesperson = Salesperson(name="BendOver", employee_id="789", salary=60000, territory="North")
print(salesperson.display_info())
print(salesperson.make_sales_pitch())
