from .base_model import BaseDocument
import mongoengine as me

class Mouse(BaseDocument):
    meta = {"collection": "mouses"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    tracking_method = me.StringField()  # Optical / Laser
    connection_type = me.StringField()  # Wired / Wireless
    max_dpi = me.IntField()
    hand_orientation = me.StringField()  # Right / Left / Ambidextrous
    color = me.StringField()
