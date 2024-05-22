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
      <button type="submit" class="btn btn-primary">작성하기</button>
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
.create-post {
  background: linear-gradient(to right, #ffffff, #e6f7ff);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: transform 0.3s, box-shadow 0.3s;
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
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-control:focus {
  border-color: #005c99;
  box-shadow: 0 0 10px rgba(0, 92, 153, 0.2);
}

.btn-primary {
  padding: 12px 24px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
