# models/gpu.py
from .base_model import BaseDocument
import mongoengine as me

class GPU(BaseDocument):
    meta = { "collection": "video_cards" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    chipset = me.StringField()
    memory = me.IntField()       # GB cinsinden
    core_clock = me.IntField()   # MHz cinsinden
    boost_clock = me.IntField()  # MHz cinsinden
    color = me.StringField()
    length = me.IntField()       # mm cinsinden
