import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    }
    else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'POST',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then(res => {
        console.log('회원가입 성공')
        const password = password1
        logIn({ username, password })
      })
      .catch(err => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    //1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    //2. axios로 로그인
    axios({
      method: 'POST',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        console.log('로그인 성공!')
        token.value = res.data.key
        console.log(token)
        router.push({ name: 'ArticleView' })
      })
      .catch(err => {
        console.log(err)
      })
    //3. 응답받은 토큰도 저장
  }
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
