<template>
  <card>
    <div class="singer-info">
      <h1>가수 이름</h1>
      <img src="@/assets/singer.jpg" alt="" class="singer-image">
      <p>가수 소개글</p>
      <div class="album-details">
        <SingerAlbum />
        <SingerAlbum />
      </div>
    </div>
  </card>
</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue'
</script>

<style scoped>
.singer-info {
  border: 1px solid black;
  text-align: center;
}

.singer-image {
  width: 200px;
  border-radius: 50%;
}

.album-details {
  margin: 30px auto;
  /* 이 값은 필요에 따라 조정하세요. */
  /* auto를 사용하여 좌우 여백을 동일하게 설정합니다. */
  display: flex;
  justify-content: center;
}

.album-details> :not(:last-child) {
  margin-right: 50px;
  /* 각 앨범 사이의 간격을 조절합니다. */
}
</style>
