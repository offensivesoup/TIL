import json
from pprint import pprint


def books_info(books, categories):
    result = []
    # categoryName으로 바꿔주기
    for book in books:
        bookNameLst = []
        book_id = book['categoryId']
        for num in book_id:
            for category in categories:
                if category['id'] == num:
                    bookNameLst.append(category['name'])
        book['categoryName'] = book.pop('categoryId')
        book['categoryName'] = bookNameLst 
    # 필요한 정보만 새 dict에 담고 리스트에 추가
    for book in books:
        dictTmp = {}
        dictTmp['author'] = book['author']
        dictTmp['categoryName'] = book['categoryName']
        dictTmp['cover'] = book['cover']
        dictTmp['description'] = book['description']
        dictTmp['id'] = book['id']
        dictTmp['priceSales'] = book['priceSales']
        dictTmp['title'] = book['title']
        result.append(dictTmp)
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
