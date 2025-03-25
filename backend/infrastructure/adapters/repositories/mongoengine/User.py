from mongoengine import DateField, Document, StringField


class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    birth = DateField(required=True)
