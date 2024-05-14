<template>
  <div class="card">
    <h1>부모 페이지입니다.</h1>
    <childPage v-for="child in children" :child="child" />
  </div>
</template>

<script setup>
import childPage from '@/components/ChildPage.vue'

const children = [
  { name: '김하나', age: 30 },
  { name: '김두리', age: 20 },
  { name: '김서이', age: 10 },
]

</script>

<style scoped>
.card {
  border: 3px outset lightgray;
  padding-left: 10px;
}
</style>