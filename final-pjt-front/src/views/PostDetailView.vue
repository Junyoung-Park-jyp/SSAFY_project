<template>
  <div>
    <div v-if="postInfo">
      <p>게시물 제목: {{ postInfo.title }}</p>
      <p>게시물 내용: {{ postInfo.content }}</p>
      <!-- 게시물 정보 표시 -->
      <div>
        <h2>댓글</h2>
        <div v-if="comments">
          <div v-for="comment in comments" :key="comment.id">
            <p>{{ comment.content }}</p>
            <p>작성자: {{ comment.author.username }}</p>
            <p>작성일자: {{ comment.created_at }}</p>
          </div>
        </div>
        <div v-else>
          <p>댓글을 불러오는 중입니다...</p>
        </div>
      </div>
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
const comments = ref(null)
const postId = route.params.postId 

const getPost = () => {
  axios.get(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/`)
    .then((res) => {
      postInfo.value = res.data
      getComments()
    })
    .catch(err => console.log(err))
}

const getComments = () => {
  axios.get(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/`)
    .then((res) => {
      comments.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(getPost)
</script>

<style scoped>
/* Your styles here */
</style>