from .base_model import BaseDocument
import mongoengine as me

class Motherboard(BaseDocument):
    meta = {"collection": "motherboards"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    socket = me.StringField()
    form_factor = me.StringField()  # Örn: ATX, Micro ATX
    max_memory = me.IntField()  # GB
    memory_slots = me.IntField()
    color = me.StringField()
