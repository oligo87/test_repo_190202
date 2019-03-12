# class Person:
#     title = "All people"
#
#     def printer_self(self):
#         print(self)
#
#     def __init__(self, x):
#         self.name = x
#
#
# if __name__ == "__main__":
#     p1 = Person('Olena')
#     p2 = Person('Vova')
#     # p1.set_name('Kolya')
#     # p2.set_name('Vasya')
#     print(p1.name)
#     print(p2.name)
#     print(p1.name is p2.name)
#     print(p1.title is p2.title)


class Person:
    def __init__(self, name='', surname='', age=18):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"<Person object with name={self.name}, "\
               f"surname={self.surname}, "\
               f"and age={self.age}>"

    def full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_older(self, years=1):
        self.age += years
        return self.age


if __name__ == "__main__":
    p1 = Person('Olena', 'Piankova')
    p2 = Person('Vova', age=23)
    print(p1.name, p1.surname, p1.age)
    print(p2.name, p2.surname, p2.age)
    print(p1.full_name())
    print(p1.get_older(2))
