<template>
  <ul>
    <ProductListItem v-for="product in products" :key="product.id" :product="product" @addToCart="addToCart" />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: Array
})
const emit = defineEmits(['addToCart'])
const addToCart = function (id) {
  emit('addToCart', id)
}
</script>
