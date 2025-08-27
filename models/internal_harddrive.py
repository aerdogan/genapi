from .base_model import BaseDocument
import mongoengine as me

class InternalHardDrive(BaseDocument):
    meta = {"collection": "internal-harddrives"}

    name = me.StringField()
    price = me.FloatField()
    capacity = me.IntField()  # GB
    price_per_gb = me.FloatField()
    type = me.StringField()  # SSD / HDD
    cache = me.IntField()  # MB
    form_factor = me.StringField()
    interface = me.StringField()
