<template>
  <div class="container create-post">
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
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">작성하기</button>
        <router-link to="/community" class="btn btn-secondary">뒤로가기</router-link>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useProductStore } from '@/stores/products';

export default {
  setup() {
    const title = ref('');
    const content = ref('');
    const productStore = useProductStore();

    const createPost = async () => {
      try {
        await productStore.createCommunity({ title: title.value, content: content.value });
        title.value = '';
        content.value = '';
      } catch (error) {
        console.error('Failed to create post:', error);
      }
    };

    return {
      title,
      content,
      createPost,
    };
  },
};
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
  margin-top: 5%;
  background: linear-gradient(to right, #e0eafc, #cfdef3);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.create-post {
  background: linear-gradient(to right, #ffffff, #e6f7ff);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 100%;
  transition: transform 0.3s, box-shadow 0.3s;
  animation: fadeIn 0.5s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.create-post:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

h1 {
  color: #005c99;
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 20px;
  border-bottom: 3px solid #005c99;
  padding-bottom: 10px;
}

.post-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  font-size: 18px;
  color: #333;
  margin-bottom: 5px;
}

.form-control {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-control:focus {
  border-color: #005c99;
  box-shadow: 0 0 10px rgba(0, 92, 153, 0.2);
}

.btn {
  padding: 12px 24px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
  transition: background-color 0.3s, box-shadow 0.3s, transform 0.3s;
}

.btn-primary {
  background-color: #005c99;
  color: white;
  border: none;
  margin-right: 10px;
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  transform: translateY(-3px);
}

.btn-primary:active {
  background-color: #003366;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

.btn-secondary {
  background-color: #cccccc;
  color: #333;
  border: none;
}

.btn-secondary:hover {
  background-color: #999999;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  transform: translateY(-3px);
}

.btn-secondary:active {
  background-color: #666666;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
</style>
