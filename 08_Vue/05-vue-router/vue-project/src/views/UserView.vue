<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 유저 홈페이지</h2>
    <h2>{{ userId }}번 유저 홈페이지</h2>
    <button @click="goHome">goHome</button>
    <button @click="routeUpdate">100번 유저 페이지로감!!</button>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import router from '@/router';
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const goHome = function () {
  // router.push({ name: 'home' })
  router.replace({ name: 'home' })
}
const route = useRoute()
const userId = ref(route.params.id)

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠날래?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 } })
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})

</script>

<style lang="scss" scoped></style>