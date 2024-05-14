<template>
  <li v-for="product in products" :key="product.id">
    <ProductItem :product="product" />
  </li>
</template>

<script setup>
import ProductItem from '@/components/ProductListItem.vue'
defineProps({
  products: Array
})
</script>
