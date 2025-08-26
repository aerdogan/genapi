# models/base_model.py
import mongoengine as me

class BaseDocument(me.Document):
    meta = {"abstract": True}
