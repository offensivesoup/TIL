<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <span>제목 : </span>
      <input type="text" v-model="title">
      <span>내용 : </span>
      <input type="text" v-model="content">
      <input type="submit" value='create'>
    </form>

  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'
import axios from 'axios'
const store = useArticleStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'POST',
    url: 'http://127.0.0.1:8000/api/v1/articles/',
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then(res => {
      console.log(res)
      router.push({ name: 'home' })
    })
    .catch(err => {
      console.log(err)
    })
}


</script>

<style scoped></style>