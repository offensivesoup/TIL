<template>
  <div>
    <main class="container py-3">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="_ in numberOfItems">
          <card />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import card from '@/components/GalleryListItem.vue'
const numberOfItems = ref(4)
</script>

<style scoped></style>