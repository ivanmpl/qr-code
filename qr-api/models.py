import mongoengine


class Qr(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    url = mongoengine.StringField(max_length=50)
    data = mongoengine.StringField(max_length=50)
