<template>
  <div>
    <ParentChild my-msg="messgae" :dynamic-props="name" @some-event="someCallBack2" @emit-args="getNumbers" />
    <ParentChild @update-name="updateName" />
    <!-- <ParentChild my-msg="messgae" :dynamic-props="name" @some-event="someCallBack2" /> -->
    <!-- <ParentItem v-for="item in items" :key="item.id" :my-prop="item" /> -->
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
// import ParentItem from '@/components/ParentItem.vue'
import { ref } from 'vue'
const name = ref('Alice')

const items = ref([
  { id: 1, name: '사과' },
  { id: 2, name: '바나나' },
  { id: 3, name: '딸기' },
])

const someCallBack = function () {
  console.log('ParentChild가 발신한 이벤트를 수신 했다.')
}
const someCallBack2 = function () {
  console.log('define 이벤트 수신')
}
const getNumbers = function (...args) {
  console.log(args)
}

const updateName = function () {
  name.value = 'Bella'
}
</script>

<style scoped></style>