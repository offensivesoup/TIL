<template>
  <div class="article">
    <h2>부모 컴포넌트</h2>
    <p>{{ familyInfo.father }}</p>
    <p>{{ familyInfo.mother }}</p>
    <ChildPage v-for="children in familyInfo.children" key="childeren.name" :children="children" />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  'familyInfo': Object
})

</script>

<style scoped>
.article {
  text-align: center;
  border: 1px solid black;
  margin: 20px;
  background-color: lightgray;
}
</style>