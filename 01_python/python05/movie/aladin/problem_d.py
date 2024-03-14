import json
from pprint import pprint


def best_book(books):
    idLst = []
    detailLst = []
    rankLst = []
    for book in books:
        idLst.append(book['id'])    
    for id in idLst:
        detail = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(detail)
        detailLst.append(book_detail)
    # 여기에 코드를 작성합니다.
    for ranking in detailLst:
        rankLst.append(ranking['customerReviewRank'])
    for user in detailLst:
        if user['customerReviewRank'] == max(rankLst):
            return user['title']

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    pprint(best_book(books_list))
