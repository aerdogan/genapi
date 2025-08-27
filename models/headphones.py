from .base_model import BaseDocument
import mongoengine as me

class Headphones(BaseDocument):
    meta = {"collection": "headphones"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    type = me.StringField()
    frequency_response = me.ListField(me.FloatField(), default=[])  # [min, max] Hz
    microphone = me.BooleanField(default=False)
    wireless = me.BooleanField(default=False)
    enclosure_type = me.StringField()
    color = me.StringField()

