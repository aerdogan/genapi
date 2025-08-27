# models/sound_card.py
from .base_model import BaseDocument
import mongoengine as me

class SoundCard(BaseDocument):
    meta = { "collection": "sound_cards" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    channels = me.FloatField()      # 2.0, 5.1, 7.1 gibi
    digital_audio = me.IntField()   # bit depth (örn: 32 bit)
    snr = me.IntField()             # Signal-to-Noise Ratio (dB)
    sample_rate = me.IntField()     # kHz
    chipset = me.StringField()
    interface = me.StringField()
