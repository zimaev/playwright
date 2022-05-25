from faker import Faker
import json


class Message(object):
    fake = Faker(['en_US'])

    def __init__(self):

        self.name = Message.fake.first_name()
        self.email = Message.fake.email()
        self.subject = Message.fake.catch_phrase()
        self.message = Message.fake.paragraph(nb_sentences=6)

    def __str__(self):
        return json.dumps(self.__dict__)
