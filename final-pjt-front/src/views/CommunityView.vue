<template>
  <div>
    <h1>커뮤니티 게시판</h1>
    <RouterLink :to="{name: 'create'}">create | </RouterLink>
    <div v-if="posts.length">
      <h2>게시물 목록</h2>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <RouterLink :to="{ name: 'post', params: { postId: post.id }}"> {{ post.title }} </RouterLink>
        </li>
      </ul>
    </div>
    <div v-else>
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