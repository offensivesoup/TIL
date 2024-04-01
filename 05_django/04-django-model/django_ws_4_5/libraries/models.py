from django.db import models
import requests

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    mallType = models.TextField()
    itemId = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.IntegerField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(Book):
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=키는하고지움&Query=aladdin&MaxResults=10&start=1&SearchTarget=Book&output=js&InputEncoding=utf-8&Version=20131101')
        data = response.json()

        for item in data['item']:
            my_model = Book(isbn = item['isbn'],
                           author = item['author'], 
                           title = item['title'],
                           mallType = item['mallType'],
                           itemId = item['itemId'],
                           price = item['priceSales'],
                           fixed_price = item['priceStandard'],
                           pub_date = item['pubDate'])
            my_model.save()


# from django.db import models
# import requests

# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     @classmethod
#     def insert_data(cls):
#         response = requests.get('https://api.example.com/data')
#         data = response.json()

#         for item in data:
#             my_model = cls(field1=item['field1'], field2=item['field2'])
#             my_model.save()

# # django shell에서 아래 코드 실행
# # MyModel.insert_data()