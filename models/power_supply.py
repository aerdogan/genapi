# models/psu.py
from .base_model import BaseDocument
import mongoengine as me

class PSU(BaseDocument):
    meta = { "collection": "power_supplies" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    type = me.StringField()
    efficiency = me.StringField()
    wattage = me.IntField()
    modular = me.StringField()   # örn: Full, Semi, Non
    color = me.StringField()
