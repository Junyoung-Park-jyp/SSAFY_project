<template>
  <div class="container mt-4 community">
    <h1>커뮤니티 게시판</h1>
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
.community {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #002b5c;
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #002b5c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #005c99;
}

.post-list {
  margin-top: 20px;
}

.post-item {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.post-link {
  text-decoration: none;
  color: #005c99;
  font-size: 18px;
}

.post-link:hover {
  color: #002b5c;
}

.no-posts {
  margin-top: 20px;
  font-size: 18px;
  color: #777;
}
</style>
