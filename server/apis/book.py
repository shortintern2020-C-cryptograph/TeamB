from flask_restful import Resource, reqparse, abort
from flask import jsonify
from models.book import BookModel, BookSchema
from database import db
from apis.searchBooks import Search_Books_API
import json
import codecs
import urllib.parse
import urllib.request
import requests

class BookListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', required=True)
        self.reqparse.add_argument('author', required=True)
        self.reqparse.add_argument('item_caption')
        self.reqparse.add_argument('image_url')
        self.reqparse.add_argument('item_url')
        self.reqparse.add_argument('image')
        super(BookListAPI, self).__init__()

    def get(self):
        results = BookModel.query.all()
        #data = urllib.parse.urlencode(results)
        #data = data.encode('ascii')
        jsonData = BookSchema(many=True).dump(results).data
        return jsonify({'items': jsonData})

    def post(self):
        args = self.reqparse.parse_args()
        book = BookModel(args.title, args.author, args.item_caption, args.image_url, args.item_url, args.image)
        db.session.add(book)
        db.session.commit()
        res = BookSchema().dump(book).data
        return res, 201
    
class GetBookListAPI(Resource):
    def get(self, key):
        search_books = Search_Books_API(keyword=key)
        #books = search_books.get_dict()
        books = search_books.get_dict()
        #hoge = codecs.open(books, 'w', 'utf-8')
        #jsonData = json.dump(books, ensure_ascii=False).data
        #jsonData = json.dumps(books, ensure_ascii=False, indent=4)
        #jsonData = json.dump(books).data
        return books
        #return jsonify({'items': jsonData})

class BookAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title')
        self.reqparse.add_argument('author')
        self.reqparse.add_argument('item_caption')
        self.reqparse.add_argument('image_url')
        self.reqparse.add_argument('item_url')
        self.reqparse.add_argument('image')
        super(BookAPI, self).__init__()

    def get(self, id):
        book = db.session.query(BookModel).filter_by(id=id).first()
        if book is None:
            abort(404)

        res = BookSchema().dump(book).data
        return res

    def put(self, id):
        book = db.session.query(BookModel).filter_by(id=id).first()
        if book is None:
            abort(404)
        args = self.reqparse.parse_args()
        for name, value in args.items():
            if value is not None:
                setattr(book, name, value)
        db.session.add(book)
        db.session.commit()
        return None, 204

    def delete(self, id):
        book = db.session.query(BookModel).filter_by(id=id).first()
        if book is not None:
            db.session.delete(book)
            db.session.commit()
        return None, 204

