from app import db


class Post(db.Model):
    """ Model for post """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __init__(self, title):
        self.title = title
