class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}."


class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age, "Manager")
        self.department = department

    def manage(self):
        return f"Manager {self.name} is managing the {self.department} department."


class Intern(Employee):
    def __init__(self, name, age, duration):
        super().__init__(name, age, "Intern")
        self.duration = duration

    def intern_info(self):
        return f"{self.name} is an intern for {self.duration} months."


class Organization:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def list_members(self):
        print(f"\nMembers of {self.name}:")
        for member in self.members:
            print(member.introduce())


if __name__ == "__main__":

    company = Organization("Tech Solutions")

    person = Person("John Doe", 30)
    employee = Employee("Jane Smith", 28, "Developer")
    manager = Manager("Alice Johnson", 40,  "IT")
    intern = Intern("Mike Brown", 22, 6)

    company.add_member(person)
    company.add_member(employee)
    company.add_member(manager)
    company.add_member(intern)

    company.list_members()
    print(manager.manage())
    print(intern.intern_info())
