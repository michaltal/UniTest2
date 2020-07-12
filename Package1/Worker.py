# class Worker
import datetime

class Worker:
    """The Worker class holds information and methods about workers"""
    def __init__(self, fname, lname, byear, bmonth, bday):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.birth_month = bmonth
        self.birth_day = bday

    def full_name(self):
        """Returns the full name of the worker"""
        return f'{self.first_name} {self.last_name}'

    def age(self):
        """Returns the age of the worker"""
        return f'{self.first_name} is {datetime.datetime.now().year - self.birth_year} years old'

    def days_to_birthday(self):
        """Returns the number of days until the next birthday"""
        now = datetime.date.today()
        if self.birth_month < int(now.month):
            new_year = int(now.year)+1
            birthday_this_year = datetime.date(new_year, self.birth_month, self.birth_day)
        else:
            birthday_this_year = datetime.date(int(now.year), self.birth_month, self.birth_day)
        return birthday_this_year - now

    def greet(self, other):
        return f'{self.first_name} says hello to {other.first_name}'




# bob = Worker('Bob', 'Marshall', 1970, 7, 5)
# print(bob.full_name())
# print(bob.first_name, 'birth year is ', bob.birth_year,'\n',bob.age())
# print('Number of days to birthday: ',bob.days_to_birthday())
# print(datetime.datetime.now().year)
# print(datetime.datetime.today())
# alice = Worker('Alice', 'Smith',1995)
# print(bob.full_name(),bob.birth_year)
# print(alice.full_name())
# print(f'{bob.full_name()} is {bob.age()} years old.')
# print(bob.greet(alice))


# bob.country = 'Israel'
# bob.city = 'Haifa'
# print(f'{bob.full_name()} is from {bob.city}, {bob.country}')

