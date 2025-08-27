# models/speaker.py
from .base_model import BaseDocument
import mongoengine as me

class Speaker(BaseDocument):
    meta = { "collection": "speakers" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    configuration = me.IntField()          # 2.0, 2.1, 5.1 gibi
    wattage = me.FloatField()              # Watt
    frequency_response = me.ListField(me.IntField())  # [min, max] Hz
    color = me.StringField()
