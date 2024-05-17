<template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="createPost">
        <label for="title">Title:</label>
        <input v-model="title" type="text" id="title">
        <label for="content">Content:</label>
        <textarea v-model="content" id="content"></textarea>
        <button type="submit">작성하기</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { useUserStore } from '@/stores/users'
  
  export default {
    data() {
      return {
        title: '',
        content: ''
      }
    },
    methods: {
      createPost() {
        const userStore = useUserStore()
        axios.post('http://127.0.0.1:8000/api/v1/community/posts/', {
          title: this.title,
          content: this.content
        }, {
          headers: { Authorization: `Token ${userStore.token}` }
        })
        .then(response => {
          console.log(response)
          this.$router.push({ name: 'community' })
        })
        .catch(error => {
          console.error(error)
        })
      }
    }
  }
  </script>
  