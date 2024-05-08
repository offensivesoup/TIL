<template>
  <header class='header'>
    <h1>Gallery</h1>
  </header>
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div class="col" v-for="item in numberOfItems" :key="item">
        <div class="card">
          <img src="../assets/sample.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
              content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'

const numberOfItems = ref(4)

</script>

<style scoped>
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(174, 231, 212);
  padding: 20px;
}
</style>
