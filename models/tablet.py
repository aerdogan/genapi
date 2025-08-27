# models/tablet.py
from .base_model import BaseDocument
import mongoengine as me

class Tablet(BaseDocument):
    meta = { "collection": "tablets" }

    name = me.StringField(required=True)
    sim = me.StringField()
    battery = me.StringField()
    ram = me.StringField()         # RAM ve depolama bilgisi string olarak
    networks = me.StringField()
    processor = me.StringField()
    screen_size = me.StringField() # ekran boyutu, çözünürlük ve Hz bilgisi
    os = me.StringField()
    camera = me.StringField()      # ön/arka kamera bilgisi
