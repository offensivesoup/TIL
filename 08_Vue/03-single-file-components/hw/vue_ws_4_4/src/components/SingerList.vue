<template>
  <div>
    <h1>가수 목록</h1>
    <Detail />
  </div>
</template>

<script setup>
import Detail from '@/components/singers/SingerDetail.vue'
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