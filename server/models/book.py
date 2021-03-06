from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from database import db

ma = Marshmallow()


class BookModel(db.Model):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    #author_id = db.Column(db.Integer, nullable=True, db.ForeignKey('authors.id)
    genre_id = db.Column(db.String(10), nullable=False)
    item_caption = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    item_url = db.Column(db.String(255), nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    thread = db.relationship("ThreadModel")

    def __init__(self, title, author, genre_id, item_caption=None, image_url=None, item_url=None, image=None):
        self.title = title
        self.author = author
        self.genre_id = genre_id
        self.item_caption = item_caption
        self.image_url = image_url
        self.item_url = item_url
        self.image = image

    def __repr__(self):
        return '<ThreadModel {}:{}:{}:{}>'.format(self.id, self.title, self.author, self.genre_id)


class BookSchema(ma.Schema):
    class Meta:
     # 欲しいデータを記述
        fields = ("id", "title", "author", "genre_id", "item_caption", "image_url", "item_url", "image")
