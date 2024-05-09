<template>
  <h2>메인 페이지</h2>
  <MainPage v-for="balances in store.balances" :key="balances.name" :balances="balances" />
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance';
import MainPage from '@/components/MainPage.vue'
const store = useBalanceStore()

</script>

<style scoped></style>