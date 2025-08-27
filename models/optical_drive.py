# models/optical_drive.py
from .base_model import BaseDocument
import mongoengine as me

class OpticalDrive(BaseDocument):
    meta = { "collection": "optical_drives" }

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    bd = me.IntField()          # Blu-ray okuma hızı
    dvd = me.IntField()         # DVD okuma hızı
    cd = me.IntField()          # CD okuma hızı
    bd_write = me.StringField() # Blu-ray yazma hızları (örn: "14/12/2/2")
    dvd_write = me.StringField()# DVD yazma hızları
    cd_write = me.StringField() # CD yazma hızları
