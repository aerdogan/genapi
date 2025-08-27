from .base_model import BaseDocument
import mongoengine as me

class Monitor(BaseDocument):
    meta = {"collection": "monitors"}

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    screen_size = me.FloatField()  # inç
    resolution = me.ListField(me.IntField(), default=[])  # [width, height]
    refresh_rate = me.IntField()  # Hz
    response_time = me.IntField()  # ms
    panel_type = me.StringField()  # IPS / VA / TN
    aspect_ratio = me.StringField()  # örn: "16:9"
