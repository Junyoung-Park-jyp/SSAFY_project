<template>
    <div>
      <h1>커뮤니티 게시판</h1>
      <CommunityCreateView />
    </div>
  </template>
  
  <script>
  import CommunityCreateView from './CommunityCreateView.vue';
  import axios from 'axios'
  
  export default {
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
  