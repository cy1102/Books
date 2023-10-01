from pymongo import MongoClient
import certifi
import requests
from bs4 import BeautifulSoup

mongo_srv = 'mongodb+srv://user:1234@cluster1.b5dbq8u.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where();
client = MongoClient(mongo_srv, tlsCAFile=ca)
db = client.rgorithm

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.goodreads.com/list/show/43.Best_Young_Adult_Books', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

infos = soup.select('#all_votes > table > tr')
for info in infos:
    book_title = info.select_one('.bookTitle > span').text
    book_author = info.select_one('.authorName > span').text
    book_cover = info.select_one('.bookCover')['src']
    book_info = {'title': book_title, 'author': "By "+ book_author, 'cover': book_cover}

    db.book.insert_one(book_info)
