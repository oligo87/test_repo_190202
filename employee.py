from person import Person


class Employee(Person):
    def __init__(self, *args, position='QA', salary=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.salary = salary

    def income(self, months=1):
        return self.salary * months

    def __str__(self):
        old = super().__str__()
        result = old.replace('Person', 'Employee')
        result = result + self.position + str(self.salary)
        return result


if __name__ == "__main__":
    e1 = Employee('Vasya', salary=1000)
    e1.full_name()
    print(e1.income(12))
    print(e1)