<template>
  <h2>장바구니</h2>
  <div v-for="product in cartProduct" :key="product.id">
    <li>
      {{ product.name }} - {{ product.price }}원
      <button @click="$emit('deleteToCart', product.id)">삭제</button>
    </li>
  </div>
</template>

<script setup>
defineProps({
  cartProduct: Array
})

const deleteToCart = function (id) {
  emit('delteToCart', id)
}
</script>

<style scoped></style>