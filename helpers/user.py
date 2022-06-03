from faker import Faker
import random
import json


class User(object):
    fake = Faker(['en_US'])

    def __init__(self):

        self.password = User.fake.password()
        self.days = str(random.randint(1, 31))
        self.months = str(random.randint(1, 12))
        self.years = str(random.randint(1900, 2021))
        self.first_name = User.fake.first_name()
        self.last_name = User.fake.last_name()
        self.company = User.fake.company()
        self.address1 = User.fake.street_address()
        self.country = random.choice(['India', 'United States',
                                      'Canada', 'Australia', 'Israel',
                                      'New Zealand', 'Singapore'])
        self.state = User.fake.street_suffix()
        self.city = User.fake.city()
        self.zipcode = User.fake.postcode()
        self.mobile_number = User.fake.phone_number()
        self.email = User.fake.email()

    def JSON_user(self):
        data = {
            "name": self.first_name,
            "email": self.email,
            "password": self.password,
            "title": random.choice(['Mr', 'Ms']),
            "birth_date": str(random.randint(1, 31)),
            "birth_month": str(random.randint(1, 12)),
            "birth_year": str(random.randint(1900, 2021)),
            "firstname": self.first_name,
            "lastname": self.last_name,
            "company": self.last_name,
            "address1": self.address1,
            "country": self.country,
            "zipcode": self.zipcode,
            "state": self.state,
            "city": self.state,
            "mobile_number": self.mobile_number
        }
        return data







