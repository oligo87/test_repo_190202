from employee import Employee


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, *new_skill):
        self.skills.append(new_skill)

    def __str__(self):
        old = super().__str__()
        result = old.replace('Employee', 'IT Employee')
        result = result + f'<Skills: {self.skills}>\n'
        return result


if __name__ == "__main__":
    ite1 = ITEmployee()
    ite1.add_skill('Python', 'Selenium')
    print(ite1)
    print(ite1.income(12))
