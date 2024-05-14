<template>
  <div class="card">
    <parent />
  </div>
</template>

<script setup>
import parent from '@/components/ParentPage.vue'
</script>

<style scoped>
.card {
  border: 3px outset lightgray;
  padding-left: 10px;
}
</style>