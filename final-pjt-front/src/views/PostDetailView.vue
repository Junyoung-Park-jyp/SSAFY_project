<template>
  <div>
    <h1>{{ postId }}번 게시물</h1>
    <div v-if="postInfo">
      <p>게시물 제목: {{ postInfo.title }}</p>
      <p>게시물 내용: {{ postInfo.content }}</p>
      <!-- 기타 게시물 정보를 여기에 표시 -->
    </div>
    <div v-else>
      <p>게시물 정보를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios';
const route = useRoute()
const postInfo = ref(null)
const postId = route.params.postId 
const getPost = () => {
  axios.get(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/`)
    .then((res) => {
      postInfo.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(getPost)
</script>
<style scoped>

</style>