<template>
  <div class="create-post-container">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">게시글 작성</h1>
      </div>
      <div class="card-body">
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
    </div>
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
.create-post-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #6dd5fa, #ffffff);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  width: 100%;
  max-width: 600px; /* 기존 크기 유지 */
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

.form-label {
  font-size: 16px;
  color: #333;
  margin-bottom: 5px;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  margin-bottom: 15px;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  border-color: #005c99;
  box-shadow: 0 0 5px rgba(0, 92, 153, 0.5);
}

.btn-primary {
  width: 100%;
  padding: 10px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #004080;
}
</style>
