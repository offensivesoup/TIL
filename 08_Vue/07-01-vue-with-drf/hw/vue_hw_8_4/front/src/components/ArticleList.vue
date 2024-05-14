<template>
  <div v-for="article in store.articles" :key="article.title">
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})


</script>

<style scoped></style>