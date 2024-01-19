import json


def best_new_books(books):
    idLst = []
    detailLst = []
    result = []
    rankLst = []
    for book in books:
        idLst.append(book['id'])    
    for id in idLst:
        detail = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(detail)
        detailLst.append(book_detail)
    for detail in detailLst:
        if int(detail["pubDate"][:4]) == 2023:
            result.append(detail)
            rankLst.append(detail['customerReviewRank'])
            if max(rankLst) == detail['customerReviewRank']:
                result = detail['title']
                return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
