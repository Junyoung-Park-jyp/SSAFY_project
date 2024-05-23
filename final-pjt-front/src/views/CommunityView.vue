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
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
  background: #f4f4f9;
  color: #333;
  margin: 0;
  padding: 0;
}

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
  background: white;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.card-header {
  background: linear-gradient(to right, #0f4c75, #3282b8);
  color: white;
  padding: 20px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.card-title {
  font-size: 28px;
  font-weight: bold;
  margin: 0;
  color: white;
}

.card-body {
  padding: 20px;
  background: #f0f9ff;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

.list-group-item {
  border: none;
  border-radius: 10px;
  margin-bottom: 10px;
  transition: transform 0.3s, box-shadow 0.3s;
  background: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.list-group-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.text-decoration-none {
  text-decoration: none;
}

.text-dark {
  color: #333 !important;
}

.badge {
  font-size: 14px;
  padding: 10px;
  border-radius: 15px;
  transition: background-color 0.3s;
  background: linear-gradient(to right, #3282b8, #0f4c75);
  color: white;
}

.btn-primary {
  background-color: #0f4c75;
  border: none;
  padding: 10px 20px;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  font-size: 18px;
  font-weight: bold;
}

.btn-primary:hover {
  background-color: #3282b8;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

h2, h4 {
  color: #0f4c75;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.shadow-lg {
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
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

/* Additional effects for buttons and badges */
.btn-primary:active {
  background-color: #0056b3;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  transform: translateY(2px);
}

.badge.bg-primary:hover {
  background-color: #0056b3;
}

/* Adding animation for list items */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.list-group-item {
  animation: fadeInUp 0.5s ease-in-out;
}

/* Button glow effect */
@keyframes glow {
  0% {
    box-shadow: 0 0 5px #0f4c75, 0 0 10px #0f4c75, 0 0 20px #0f4c75, 0 0 40px #0f4c75;
  }
  50% {
    box-shadow: 0 0 20px #3282b8, 0 0 30px #3282b8, 0 0 40px #3282b8, 0 0 50px #3282b8;
  }
  100% {
    box-shadow: 0 0 5px #0f4c75, 0 0 10px #0f4c75, 0 0 20px #0f4c75, 0 0 40px #0f4c75;
  }
}

.btn-primary:hover {
  animation: glow 1.5s infinite;
}
</style>
