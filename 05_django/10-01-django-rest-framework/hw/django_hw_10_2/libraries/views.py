from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
# Create your views here.

@api_view(['GET'])
def libraries(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def libraries_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
