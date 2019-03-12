from employee import Employee


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, *new_skill):
        self.skills.append(new_skill)


ite1 = ITEmployee(name='Oleg', surname='Ilin', age=31, position='QA', salary=1000)
ite1.add_skill('Python', 'Selenium')
print(ite1.income(12))
print(ite1)
print(ite1.skills)
