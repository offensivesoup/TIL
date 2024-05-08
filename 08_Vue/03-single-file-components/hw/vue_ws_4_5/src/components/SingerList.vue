<template>
  <h1>가수 목록</h1>
  <div v-for="singer in singers">
    <Detail />
  </div>
</template>

<script setup>
import Detail from '@/components/singers/SingerDetail.vue'
const singers = [
  { name: 'adele' },
  { name: 'maroon 5' },
  { name: 'Dua Lipa' },
]
</script>

<style scoped>
card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}

h1 {
  color: orange
}
</style>