<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <textarea v-model="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'POST',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then(res => {
      console.log(res)
      console.log(res.data)
      router.push({ name: 'ArticleView' })
    })
    .catch(res => {
      console.log(err)
    })
}

</script>

<style></style>
