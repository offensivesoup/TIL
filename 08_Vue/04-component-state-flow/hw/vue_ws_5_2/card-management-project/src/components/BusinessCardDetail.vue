<template>
  <div class="card">
    <h3>이름 : {{ card.name }}</h3>
    <p>직함 : {{ card.title }}</p>
  </div>
</template>

<script setup>
defineProps({
  card: Object
})
</script>

<style scoped>
.card {
  background-color: lightgray;
  padding: 20px;
  margin: 15px;
  text-align: center;
}
</style>