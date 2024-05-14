<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @addToCart="addToCart" />
    <p>총 가격 : {{ totalPrice() }}원</p>
    <Cart :cart-product="cartProduct" @deleteToCart="deleteToCart" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'
let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cartProduct = ref([])

const addToCart = function (productId) {
  const productToAdd = products.value.find(product => product.id === productId)
  cartProduct.value = [...cartProduct.value, productToAdd]
}

const deleteToCart = function (productId) {
  const productToDelete = products.value.find(product => product.id === productId)
  cartProduct.value.splice(productToDelete, 1)
}

const totalPrice = function () {
  return cartProduct.value.reduce((total, product) => total + product.price, 0)
}
</script>
