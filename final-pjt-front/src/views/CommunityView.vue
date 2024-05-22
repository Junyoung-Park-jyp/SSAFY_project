<template>
  <div class="container mt-4">
    <div class="card shadow-lg rounded-3d">
      <div class="card-header bg-primary text-white rounded-top-3d">
        <h2 class="card-title mb-0">커뮤니티 게시판</h2>
      </div>
      <div class="card-body">
        <h4>게시물 목록</h4>
        <ul class="list-group">
          <li v-for="post in posts" :key="post.id" class="list-group-item d-flex justify-content-between align-items-center rounded-3d shadow-sm">
            <router-link :to="'/community/' + post.id" class="text-decoration-none text-dark">{{ post.title }}</router-link>
            <span class="badge bg-primary rounded-pill">댓글: {{ post.comments.length }}</span>
          </li>
        </ul>
        <router-link to="/create" class="btn btn-primary mt-3 shadow-lg rounded-3d">게시글 작성</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const posts = ref([]);

const loadPosts = async () => {
  const response = await axios.get('http://127.0.0.1:8000/api/v1/community/posts/');
  posts.value = response.data;  
};

onMounted(() => {
  loadPosts();
});
</script>

<style scoped>
.container {
  background: linear-gradient(to right, #e0eafc, #cfdef3);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.card {
  border: none;
  border-radius: 15px;
  overflow: hidden;
  transform: translateZ(0);
}

.card-header {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.card-title {
  font-size: 24px;
  font-weight: bold;
  margin: 0;
}

.list-group-item {
  border: none;
  border-radius: 10px;
  margin-bottom: 10px;
  transition: transform 0.3s;
}

.list-group-item:hover {
  transform: translateY(-5px);
}

.btn-primary {
  background-color: #007bff;
  border: none;
  padding: 10px 20px;
  border-radius: 15px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.btn-primary:hover {
  background-color: #0056b3;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

h2, h4 {
  color: #fff;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.rounded-3d {
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s, transform 0.3s;
}

.rounded-3d:hover {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transform: translateY(-5px);
}
</style>
