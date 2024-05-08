<template>
  <div class="titles">
    <h3 style="color:orange"> 앨범 제목 </h3>
    <p> 노래 목록 1 </p>
    <p> 노래 목록 2</p>
    <p> 노래 목록 3 </p>
  </div>
</template>

<script setup>

</script>

<style scoped>
.titles {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100px;
  background-color: lightgray;
  border: 1px darkgray solid;
  border-radius: 15%;
}
</style>