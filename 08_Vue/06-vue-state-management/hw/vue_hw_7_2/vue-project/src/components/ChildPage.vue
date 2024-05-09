<template>
  <div class="child-article">
    <h3>자식 페이지</h3>
    {{ children.name }}
  </div>
</template>

<script setup>
defineProps({
  'children': Object
})
</script>

<style scoped>
.child-article {
  text-align: center;
  border: 1px solid black;
  margin: 20px;
  padding: 50px;
  background-color: white;
}
</style>