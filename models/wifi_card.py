# models/wifi_card.py
from .base_model import BaseDocument
import mongoengine as me

class WifiCard(BaseDocument):
    meta = { "collection": "wifi_cards" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    protocol = me.StringField()
    interface = me.StringField()
    color = me.StringField()
