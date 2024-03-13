import requests
from pprint import pprint 

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbjssy06141212001'
params = {
    'ttbkey': API_KEY,
    'QueryType' : 'Bestseller',
    'start' : 1,
    'MaxResult' : 50,
    'SearchTarget' : 'Book',
    'Output' : 'JS',
    'Version' : 20131101
}
response = requests.get(API_URL, params=params)
result = response.json()
books = []
for item in result['item']:
    book = {}
    book['국제 표준 도서 번호'] = item['isbn']
    book['저자'] = item['author']
    book['제목'] = item['title']
    book['출간일'] = item['pubDate']
    books.append(book)
    
# pprint(books)
pprint(result)