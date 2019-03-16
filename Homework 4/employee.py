from person import Person


class Employee(Person):
    def __init__(self, *args, position='QA Engineer', salary=1000, experience=3, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.salary = salary
        self.experience = experience

    def get_grade(self):
        if self.experience < 3:
            grade = 'Junior'
        elif 3 <= self.experience < 6:
            grade = 'Middle'
        else:
            grade = 'Senior'
        return f'Grade is: {grade} {self.position}'

    def income(self, months=1):
        return self.salary * months

    def promotion(self, increase=0):
        self.salary += increase
        return f'New salary is: {self.salary}'

    def __str__(self):
        old = super().__str__()
        result = old.replace('Person', 'Employee')
        result = result + f'<Grade: {self.position}>\n' + f'<Salary: {str(self.salary)}>\n'
        return result


if __name__ == "__main__":
    e1 = Employee('Vasya', salary=1000, experience=5)

    print(e1.get_grade())
    print(e1.promotion(500))
