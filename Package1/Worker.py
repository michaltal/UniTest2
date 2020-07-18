# class Worker
import datetime
import requests

class Worker:
    """The Worker class holds information and methods about workers"""
    def __init__(self, fname, lname, byear, bmonth, bday,adr, country):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.birth_month = bmonth
        self.birth_day = bday
        self.address = adr
        self.cntry = country

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
        return str(birthday_this_year - now)

    def greet(self, other):
        return f'{self.first_name} says hello to {other.first_name}'

    def location(self):
        #response = requests.get(f'https://geocode.xyz/?locate='{self.address}', '{self.cntry}' & json = 1')
        param = self.address + ',' + self.cntry
        #print(param)
        url = f'https://geocode.xyz/?locate={param} &json=1'
        #url = "https://geocode.xyz/?locate=2 Dizengof, Tel Aviv, il&json=1"
        #print(url)
        payload = {}
        headers = {
          'Cookie': '__cfduid=db7a3a4e2ae670bba0d182afaf4d2cc2f1592807975; xyzh=xyzh'
        }

        #response = requests.request("GET", url, headers=headers, data = payload)
        response = requests.get(url)

        if response.ok:
            return response.text
        else:
            return 'Bad response!'



#bob = Worker('Bob', 'Marshall', 1970, 7, 30, '2 Dizengof, Tel Aviv', 'il')
#print(bob.location())
#print(bob.full_name())
#print (bob.days_to_birthday())
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

