<template>
  <div class="container mt-4 create-post">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createPost" class="post-form">
      <div class="form-group">
        <label for="title" class="form-label">제목:</label>
        <input v-model="title" type="text" id="title" class="form-control">
      </div>
      <div class="form-group">
        <label for="content" class="form-label">내용:</label>
        <textarea v-model="content" id="content" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">작성하기</button>
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

<style scoped>
.create-post {
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

.post-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  font-size: 16px;
  color: #555;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
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
</style>
