<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="$emit('addToCart', product.id)">장바구니에 추가</button>
  </li>
</template>

<script setup>
defineProps({
  product: Object
})

const emit = defineEmits(['addToCart'])
const addToCart = function (id) {
  emit('addToCart', id)
}

</script>

<style scoped></style>