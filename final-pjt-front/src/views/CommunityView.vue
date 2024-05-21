<template>
  <div class="community-container">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">커뮤니티 게시판</h1>
      </div>
      <div class="card-body">
        <RouterLink :to="{ name: 'create' }" class="btn btn-primary">게시글 작성</RouterLink>
        <div v-if="posts.length" class="post-list">
          <h2>게시물 목록</h2>
          <ul>
            <li v-for="post in posts" :key="post.id" class="post-item">
              <RouterLink :to="{ name: 'post', params: { postId: post.id }}" class="post-link">
                {{ post.title }}
              </RouterLink>
            </li>
          </ul>
        </div>
        <div v-else class="no-posts">
          <p>게시물이 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {
  components: {
    RouterLink
  },
  data() {
    return {
      posts: []
    }
  },
  methods: {
    fetchPosts() {
      axios.get('http://127.0.0.1:8000/api/v1/community/posts/')
        .then(response => {
          this.posts = response.data
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  mounted() {
    this.fetchPosts()
  }
}
</script>

<style scoped>
.community-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #6dd5fa, #ffffff);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  width: 100%;
  max-width: 800px; /* 넉넉한 크기 */
  padding: 20px;
  margin-bottom: 20%;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
}

.card-header {
  text-align: center;
  margin-bottom: 20px;
}

.card-title {
  font-size: 28px;
  color: #005c99;
  font-weight: bold;
}

.card-body {
  padding: 20px;
}

h2 {
  color: #005c99;
  font-size: 24px;
  margin-bottom: 20px;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-bottom: 20px;
}

.btn-primary:hover {
  background-color: #004080;
}

.post-list {
  margin-top: 20px;
}

.post-item {
  padding: 10px;
  border-bottom: 1px solid #ccc;
  list-style: none;
}

.post-link {
  text-decoration: none;
  color: #005c99;
  font-size: 18px;
}

.post-link:hover {
  color: #004080;
}

.no-posts {
  margin-top: 20px;
  font-size: 18px;
  color: #777;
  text-align: center;
}
</style>
