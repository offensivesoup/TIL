<template>
  <div class="card">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  'child': Object
}
)
</script>

<style scoped>
.card {
  border: 3px outset lightgray;
  padding-left: 10px;
}
</style>