<template>
  <div>
    <li>
      {{ product.name }} - {{ product.price }}원
    </li>
  </div>
</template>

<script setup>
defineProps({
  product: String
})
</script>

<style scoped></style>