from mongoengine import connect

def init_db():
    connect(db='envanter', host='localhost', port=27017)
