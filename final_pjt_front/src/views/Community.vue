<template>
    <div>
      <h1>Community</h1>
      <router-link to="/community/new">New Post</router-link>
      <div v-for="post in posts" :key="post.id">
        <router-link :to="'/community/' + post.id">
          {{ post.title }} by {{ post.author.username }}
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        posts: [],
      };
    },
    async created() {
      const response = await axios.get('http://localhost:8000/api/community/');
      this.posts = response.data;
    }
  };
  </script>
  