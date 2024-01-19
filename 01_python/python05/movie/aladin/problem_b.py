import json
from pprint import pprint


def book_info(book, categories):
    bookNameLst = []
    book_id = book['categoryId']
    for num in book_id:
        for category in categories:
            if category['id'] == num:
                bookNameLst.append(category['name'])
    book['categoryName'] = book.pop('categoryId')
    book['categoryName'] = bookNameLst
    return book, categories
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
