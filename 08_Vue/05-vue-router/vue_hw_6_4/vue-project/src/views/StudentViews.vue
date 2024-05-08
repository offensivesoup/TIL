<template>
  <h2>학생 상세 정보 목록 입니다.</h2>
  <div v-for="human in  people " :key="human.name">
    <RouterLink :to="{ name: 'student-detail', params: { name: human.name } }" class="router-link">{{ human.name
    }}의 학생 정보 보기
    </RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
const people = [
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' },
]
</script>



<style scoped>
.router-link {
  color: black;
  text-decoration: none;
  display: block;
  margin-bottom: 10px;
}
</style>
