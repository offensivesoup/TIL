## 금융 상품 데이터를 활용한 REST API 구축 (with DRF)

### 개요.

1. 사용한 라이브러리

- request, rest_framework

2. 금융상품통합비교공시 API를 사용하였다.

## 설계

- 모델

1. DepositProducts (금융상품)

2. DepositOptions (금융옵션)

=> 각 모델들은 rest_framework 의 Serializer 를 통해 Json형태로 변환하였습니다.

- URL

1. /finlife/save-deposit-products/
  - 정기 예금 상품의 저장
2. /finlife/deposit-products/
  - 전체 정기예금 상품 목록 출력 & 데이터 삽입
3. /finlife/deposit-product-options/<str:fin_prdt_cd>
  - 특정 사움의 옵션 리스트 출력
4. /finlife/deposit-products/top_rate
  - 가입 기간 상관없이 최고 금리가 높은 금융 상품과 해당 상품 옵션 리스트 출력