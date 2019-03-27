import datetime


class Person:
    def __init__(self, yob=2000, fullname='Ivan Ivanov'):
        self.full_name = fullname
        self.year_of_birth = yob
        self.now = datetime.datetime.now()

    def __str__(self):
        return f"<Person object: {self.full_name}>\n"

    def get_name(self):
        x = self.full_name.split()
        return f'Name: {x[0]}'

    def get_surname(self):
        x = self.full_name.split()
        return f'Surname: {x[1]}'

    def age_in(self):
        now = datetime.datetime.now()
        age = now.year - self.year_of_birth
        return f'Age in {now.year} year: {age}'


if __name__ == "__main__":
    p1 = Person(int(input("Enter Year of birth: ")), input("Enter Name: "))
    print(p1.get_name())
    print(p1.get_surname())
    print(p1.age_in())
