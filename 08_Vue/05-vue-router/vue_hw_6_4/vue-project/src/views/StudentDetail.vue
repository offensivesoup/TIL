<template>
  <div>
    <h2>학생 상세 정보 페이지 입니다.</h2>
    <p>이름 : {{ userName }}</p>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const userName = ref(route.params.name)
console.log(route)
</script>

<style scoped></style>