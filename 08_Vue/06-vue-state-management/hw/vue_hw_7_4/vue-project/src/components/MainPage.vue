<template>
  <div>
    <p>이름 : {{ balances.name }}</p>
    <p>잔고 : {{ balances.balance }}</p>
    <button @click="goUpdate(balances)">UpdateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goUpdate = function (balances) {
  router.push({ name: 'update', params: { name: balances.name } })
}

defineProps({
  balances: Object
})
</script>

<style scoped></style>

