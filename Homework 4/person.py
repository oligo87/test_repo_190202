class Person:
    def __init__(self, yob=2000, fullname='Ivan Ivanov'):
        self.full_name = fullname
        self.year_of_birth = yob

    def __str__(self):
        return f"<Person object: {self.full_name}>\n"

    def get_name(self):
        x = self.full_name.split()
        return f'Name: {x[0]}'

    def get_surname(self):
        x = self.full_name.split()
        return f'Surname: {x[1]}'

    def age_in(self, year=2019):
        age = year - self.year_of_birth
        return f'Age in {year} year: {age}'


if __name__ == "__main__":
    p1 = Person(1987, 'John Smith')

    print(p1.get_name())
    print(p1.get_surname())
    print(p1.age_in(2001))
