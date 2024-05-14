<template>
  <div>
    <p>{{ myMsg }}</p>
    <!-- <p>{{ dynamicProps }}</p> -->
    <ParentChildChild @update-name="updateName" />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클클릭</button>
    <button @click="emitArgs">클클클릭</button>
  </div>
</template>

<script setup>
import ParentChildChild from '@/components/ParentChildChild.vue';
// 객체 타입
defineProps({
  'myMsg': String
})
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])
const buttonClick = function () {
  emit('someEvent')
}
const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

</script>

<style scoped></style>