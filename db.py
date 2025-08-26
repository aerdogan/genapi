from mongoengine import connect

def init_db():
    connect(db='testdb', host='localhost', port=27017)
