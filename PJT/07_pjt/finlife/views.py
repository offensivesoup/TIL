# Django import
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# local import
from .models import DepositProducts, DepositOptions
from .serializer import DepositProductsSerializer, DepositOptionsSerializer

# rest_framework import
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# library import
import requests
import io

API_KEY = settings.API_KEY
BASE_URL = "http://finlife.fss.or.kr/finlifeapi/"

# Create your views here.

@api_view(['GET'])
def save(request):
    product = DepositProducts()
    option = DepositOptions()
    url = BASE_URL + "depositProductsSearch.json"
    page = input('페이지를 입력해주세요')
    params = {
        "auth" : API_KEY,
        "topFinGrpNo" : "020000",
        "pageNo" : page
    }
    response = requests.get(url, params = params).json()
    
    for data in response['result']['baseList']:
        
        product = DepositProducts(
            fin_prdt_cd=data.get('fin_prdt_cd', ''),
            kor_co_nm=data.get('kor_co_nm', ''),
            fin_prdt_nm=data.get('fin_prdt_nm', ''),
            etc_note=data.get('etc_note', ''),
            join_deny=data.get('join_deny', False),
            join_member=data.get('join_member', ''),
            join_way=data.get('join_way', ''),
            spcl_cnd=data.get('spcl_cnd', '')
        )
        product.save()
        
    for option_data in response['result']['optionList']:
        product = DepositProducts.objects.get(fin_prdt_cd=option_data.get('fin_prdt_cd'))
        if product:
            option = DepositOptions(
                fin_prdt_cd=option_data.get('fin_prdt_cd', ''),
                intr_rate_type_nm=option_data.get('intr_rate_type_nm', ''),
                intr_rate=option_data.get('intr_rate', 0.0),
                intr_rate2=option_data.get('intr_rate2', 0.0),
                save_trm=option_data.get('save_trm', -1),
                product=product  # Assigning the correct product reference
            )
            option.save()
    return JsonResponse({"message": "Data saved successfully"})

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(
            products, many = True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            if 'non_field_errors' in serializer.errors:
                return Response({"message": "이미 존재하는 데이터입니다."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "잘못된 데이터가 입력되었습니다.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def option_list(request,fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd = fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def top_rated(request):
    option = DepositOptions.objects.all().order_by('-intr_rate2').first()
    product = DepositProducts.objects.get(pk=option.product_id)

    # Option과 Product를 각각 serializer로 변환
    option_serializer = DepositOptionsSerializer(option)
    product_serializer = DepositProductsSerializer(product)

    # 두 serializer의 data를 합치기
    data = {
        "product": product_serializer.data,
        "option": [option_serializer.data]
    }
    return JsonResponse(data, status=status.HTTP_200_OK)