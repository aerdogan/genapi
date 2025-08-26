from .base_model import BaseDocument
import mongoengine as me

class User(BaseDocument):
    username = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True)
