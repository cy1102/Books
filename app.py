from flask import Flask, request, url_for, redirect, render_template, request
from pymongo import MongoClient
import certifi

mongo_srv = 'mongodb+srv://user:1234@cluster1.b5dbq8u.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_srv)

ca = certifi.where();

client = MongoClient(mongo_srv, tlsCAFile=ca)
db = client.rgorithm

app = Flask(__name__)

@app.route('/books')
def get_books():
    all_books = list(db.book.find({}))
    for book in all_books:
        print(book)
    return 'Hello World!'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/aboutpage')
def aboutpage():
    return render_template('aboutpage.html')


@app.route('/')
def home():
    return render_template('books.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
