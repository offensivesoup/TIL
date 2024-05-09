<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ name }}</p>
    <p>잔고 : {{ userBalance[0].balance }}</p>
    <button @click="store.upBalance(name)">+</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance';

const store = useBalanceStore()
const balances = store.balances
const route = useRoute()
const name = ref(route.params.name)
const userBalance = computed(() => {
  return balances.filter(balance => balance.name === name.value);
});

</script>

<style scoped></style>