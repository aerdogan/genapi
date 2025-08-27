from .base_model import BaseDocument
import mongoengine as me

class Keyboard(BaseDocument):
    meta = {"collection": "keyboards"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    style = me.StringField()
    switches = me.StringField()
    backlit = me.StringField()  # Örn: RGB
    tenkeyless = me.BooleanField(default=False)
    connection_type = me.StringField()  # Wired / Wireless
    color = me.StringField()

