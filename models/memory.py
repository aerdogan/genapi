from .base_model import BaseDocument
import mongoengine as me

class Memory(BaseDocument):
    meta = {"collection": "memories"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    speed = me.ListField(me.IntField(), default=[])  # [min, max] MHz
    modules = me.ListField(me.IntField(), default=[])  # [count, size] örn: [2, 8]
    price_per_gb = me.FloatField()
    color = me.StringField()
    first_word_latency = me.IntField()
    cas_latency = me.IntField()
