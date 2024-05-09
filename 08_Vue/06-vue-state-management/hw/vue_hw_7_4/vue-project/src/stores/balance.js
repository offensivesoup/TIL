import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('counter', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
  ])
  const upBalance = function (name) {
    const user = balances.value.find(user => user.name === name)
    user.balance += 1000
  }

  return { balances, upBalance }
})
