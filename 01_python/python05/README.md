# Finance PJT

1. 전체 정기예금 응답을 json으로 받아와 key 값을 출력한다.

- api_key를 활용하고, requests를 import 시켜 get하는 방식을 확인해볼 수 있다.

```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "{자기키 넣기}"
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.

    data = requests.get(f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1').json()
    result = data['result'].keys()
    return result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

```

2. 전체 정기예금 상품 리스트를 출력한다.

- 1번 문제와 같지만, 자료구조에 따라 인덱싱이나 혹은 키값을 통해 원하는 자료를 가져올 수 있다.

```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "{자기키 넣기}"
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    data = requests.get(f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1').json()
    result = data['result']['optionList']
    return result
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
```

3. 정기 예금 상품들의 옵션 리스트를 출력한다.

- 가져온 값을 활용하기 위해 필요한 자료로 새롭게 할당하는 방식을 알고, 해당 딕셔너리를 유지시키기 위해 리스트에 append 시키는 작동을 시켜보았다.

```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "{자기키 넣기}"
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    resultDict = {}
    result = []
    data = requests.get(f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1').json()
    optionLst = data['result']['optionList']
    for option in optionLst:
        resultDict = {}
        resultDict['금융상품코드'] = option['fin_prdt_cd']
        resultDict['저축금리'] = option['intr_rate']
        resultDict['저축기간'] = option['save_trm']
        resultDict['저축금리유형'] = option['save_trm']
        resultDict['저축금리유형명'] = option['intr_rate_type_nm']
        resultDict['최고 우대금리'] = option['intr_rate2']
        result.append(resultDict)
    return result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

```

4. 특정 자료구조로 변환시키기

- 복잡한 자료구조의 경우, 얼마의 리스트와 딕셔너리가 필요하고, 해당 자료와 일치한다는 조건을 추가하여, 맞을 경우 새롭게 자료로 할당하여 리스트에 append 시키는 방식등을 확인할 수 있다.

```python
def get_deposit_products():
    api_key = "{자기키 넣기}"
    data = requests.get(f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1').json()
    optionLst = data['result']['optionList']
    add_result = []
    finalDict = {}
    for name in data['result']['baseList']:
        finalDict = {}
        option_result = []
        finalDict['금융회사명'] = name['kor_co_nm']
        finalDict['금융상품명'] = name['fin_prdt_nm']
        num = name['fin_prdt_cd']
        for option in optionLst: 
            resultDict = {}
            if option['fin_prdt_cd'] == num:
                resultDict['저축금리'] = option['intr_rate']
                resultDict['저축기간'] = option['save_trm']
                resultDict['저축금리유형'] = option['save_trm']
                resultDict['저축금리유형명'] = option['intr_rate_type_nm']
                resultDict['최고 우대금리'] = option['intr_rate2']
                option_result.append(resultDict)
        finalDict['금리정보'] = option_result
        add_result.append(finalDict)
    return add_result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
```

----
----
----


# Movie Project

#### finanace PJT와 달리 파일에서 필요한 데이터를 가져왔다.(open과 json활용)

1. 특정 데이터 가져오기

- 필요한 정보로 딕셔너리를 재할당 하는 방식을 안다.

```python

import json
from pprint import pprint


def book_info(book):
    result = {}
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    result['author'] = book['author']
    result['id'] = book['id']
    result['priceSales'] = book['priceSales']
    result['description'] = book['description']
    result['cover'] = book['cover']
    result['categoryId'] = book['categoryId']
    result['title'] = book['title']
    return result
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))

```

2. 특정 데이터를 다른 json 과 비교하여 알맞은 값을 할당한다.

- 특정 딕셔너리 key 값을 변경시키기 위해 pop을 사용하는 방법을 알게 되었다.

```python
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
```   


3. 지난 코드에서 필요한 데이터만 dict에 담고 리스트로 추가한다.

- 2번 코드와 1번 코드를 재사용하여 필요한 코드를 재사용시, 높은 생산성을 얻을 수 있는 것을 직접 확인할 수 있었다.

```python
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
```

4. 반복문을 활용하여 해당 파일들을 열기

- f스트링을 활용하여, 반복문과 해당 파일 명들의 공통값을 찾아 반복적으로 열 수 있게 되었다.
- 크롤링 시에도 특정 페이지네이션을 위한 f스트링을 사용할 수 있을 것으로 보인다.


```python
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

```

5. 4번 코드에 조건 추가하기

- 코드의 재활용과, 조건문 추가를 통해 더욱 구체적인 데이터를 확보하는 방식을 알아보았다.


```python
import json
from pprint import pprint


def new_books(books):
    idLst = []
    detailLst = []
    result = []
    for book in books:
        idLst.append(book['id'])    
    for id in idLst:
        detail = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(detail)
        detailLst.append(book_detail)
    for detail in detailLst:
        if int(detail["pubDate"][:4]) == 2023:
            result.append(detail['title'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    pprint(new_books(books_list))
```

6. 5번에 조건 추가하는 문제.

```python
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
```
