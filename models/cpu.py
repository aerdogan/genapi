# models/cpu.py
from .base_model import BaseDocument
import mongoengine as me

class CPU(BaseDocument):
    meta = {"collection": "cpus"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    core_count = me.IntField()
    core_clock = me.FloatField()
    boost_clock = me.FloatField()
    tdp = me.IntField()
    graphics = me.StringField(null=True)
    smt = me.BooleanField(default=False)
