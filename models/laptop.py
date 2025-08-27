from .base_model import BaseDocument
import mongoengine as me

class Laptop(BaseDocument):
    meta = { "collection": "laptops" }
    model_name = me.StringField()
    brand = me.StringField()
    processor_name = me.StringField()
    ram = me.IntField()
    ssd = me.IntField()
    hdd = me.IntField(default=0)
    operating_system = me.StringField()
    graphics = me.StringField()
    screen_size = me.FloatField()
    resolution = me.StringField()
    core_count = me.IntField()
