<template>
  <div class="card">
    <h3>이름 : {{ card.name }}</h3>
    <p>직함 : {{ card.title }}</p>
    <button @click="buttonDelete(card.name)">명함삭제</button>
  </div>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue';
const emit = defineEmits(['buttonDelete',])

defineProps({
  card: Object
})

const buttonDelete = function (name) {
  emit('buttonDelete', name)
}
</script>

<style scoped>
.card {
  background-color: lightgray;
  padding: 20px;
  margin: 15px;
  text-align: center;
}
</style>