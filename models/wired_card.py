# models/pci_card.py
from .base_model import BaseDocument
import mongoengine as me

class PciCard(BaseDocument):
    meta = { "collection": "wired_cards" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    interface = me.StringField()
    color = me.StringField(null=True)
