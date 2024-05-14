<template>
  <div class="article">
    <header class="header">
      <div>
        <h1>명함 관리 페이지</h1>
      </div>
    </header>
    <main>
      <article>
        <p>명함을 관리하는 페이지 입니다. 여기에 명함 목록이 표시됩니다.</p>
      </article>
    </main>
    <card>
      <BusinessCard />
    </card>
    <footer class="footer">
      <p>@ 2023 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue'
</script>

<style scoped>
.article {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  color: white;
  background-color: rgb(53, 53, 232);
  text-align: center;
  width: 300px;
}

.footer {
  text-align: center;
  background-color: gainsboro;
  width: 100%;
  position: fixed;
  bottom: 0%;
}
</style>