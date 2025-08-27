# models/case.py
from .base_model import BaseDocument
import mongoengine as me

class Case(BaseDocument):
    meta = { "collection": "cases" }

    name = me.StringField()
    price = me.FloatField()
    type = me.StringField()
    color = me.StringField()
    psu = me.StringField(null=True)
    side_panel = me.StringField()
    external_525_bays = me.IntField(default=0)
    internal_35_bays = me.IntField(default=0)
