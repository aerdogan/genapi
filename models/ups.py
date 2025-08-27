# models/ups.py
from .base_model import BaseDocument
import mongoengine as me

class UPS(BaseDocument):
    meta = { "collection": "ups" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    capacity_w = me.IntField()  # Watt cinsinden
    capacity_va = me.IntField() # VA cinsinden
