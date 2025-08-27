# models/external_drive.py
from .base_model import BaseDocument
import mongoengine as me

class ExternalDrive(BaseDocument):
    meta = { "collection": "external_harddrives" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    type = me.StringField()
    interface = me.StringField()
    capacity = me.IntField()  # GB cinsinden
    price_per_gb = me.FloatField()
    color = me.StringField()
