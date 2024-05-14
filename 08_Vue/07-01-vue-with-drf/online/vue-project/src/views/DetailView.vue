<template>
  <div>
    <h1>DETAIL VIEW</h1>
    <div v-if="article">
      <p>글 번호 : {{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>수정시간 : {{ article.created_at }}</p>
      <p>작성시간 : {{ article.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>

import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
onMounted(() => {
  axios({
    method: 'GET',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
    .then(res => {
      article.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
})

</script>

<style></style>
