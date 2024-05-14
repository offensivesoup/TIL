<template>
  <div style="text-align: center;">
    <h2>보유 명함 목록</h2>
    <BusinessDetail v-for="card in businessCards" :key="card.name" :card="card" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BusinessDetail from '@/components/BusinessCardDetail.vue'
const businessCards = ref([
  { name: '일론 마스크', title: '테스윽라' },
  { name: '레슬링 엘리숭', title: '사랑클' },
  { name: '빌 게이췩췩', title: '빅소프트 공동창업주' },
  { name: '래리 애플파이지', title: '한글 공동창업주' },
  { name: '세링게티 브레인', title: '한글 공동창업주' }
])
</script>

<style scoped></style>