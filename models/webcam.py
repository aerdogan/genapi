# models/webcam.py
from .base_model import BaseDocument
import mongoengine as me

class Webcam(BaseDocument):
    meta = { "collection": "webcams" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    resolutions = me.ListField(me.StringField())
    connection = me.StringField()
    focus_type = me.StringField()
    os = me.ListField(me.StringField())
    fov = me.IntField()  # Field of View (derece cinsinden)
