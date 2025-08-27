# models/operating_system.py
from .base_model import BaseDocument
import mongoengine as me

class OperatingSystem(BaseDocument):
    meta = { "collection": "os" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    mode = me.IntField()         # 32-bit / 64-bit
    max_memory = me.IntField()   # Maksimum desteklenen RAM (GB)
