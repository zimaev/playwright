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

    def __str__(self):
        return json.dumps(self.__dict__)







