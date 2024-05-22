<template>
  <div class="community-container">
    <div class="card">
      <div class="card-header">
        <h1 class="card-title">커뮤니티 게시판</h1>
      </div>
      <div class="card-body">
        
        <div v-if="posts.length" class="post-list">
          <h2>게시물 목록</h2>
          <ul>
            <li v-for="post in posts" :key="post.id" class="post-item">
              <RouterLink :to="{ name: 'post', params: { postId: post.id }}" class="post-link">
                <span class="post-title">{{ post.title }}</span>
                <span class="comment-count">댓글: {{ post.comment_count }}</span>
              </RouterLink>
            </li>
          </ul>
          <RouterLink :to="{ name: 'create' }" class="btn btn-primary">게시글 작성</RouterLink>
        </div>
        <div v-else>
          <p>게시물이 없습니다.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/products';

export default {
  setup() {
    const posts = ref([]);
    const productStore = useProductStore();

    const fetchPosts = async () => {
      try {
        await productStore.getPosts();
        posts.value = productStore.posts;
      } catch (error) {
        console.error('Failed to fetch posts:', error);
      }
    };

    onMounted(fetchPosts);

    return {
      posts,
    };
  },
};
</script>

<style scoped>
.community-container {
  margin-left: auto;
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
}

.card {
  width: 100%;
  max-width: 900px;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.2);
}

.card-header {
  text-align: center;
  margin-bottom: 20px;
}

.card-title {
  font-size: 32px;
  color: #005c99;
  font-weight: bold;
}

.card-body {
  padding: 20px;
}

h2 {
  color: #005c99;
  font-size: 28px;
  margin-bottom: 20px;
}

.btn-primary {
  display: inline-block;
  padding: 12px 24px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  margin-bottom: 20px;
  text-align: center;
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.post-list {
  margin-top: 20px;
}

.post-item {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  list-style: none;
  transition: background-color 0.3s;
}

.post-item:hover {
  background-color: #f0f8ff;
}

.post-link {
  text-decoration: none;
  color: #005c99;
  font-size: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.post-link:hover {
  color: #002b5c;
}

.post-title {
  font-weight: bold;
}

.comment-count {
  color: #888;
  font-size: 18px;
}

.no-posts {
  margin-top: 20px;
  font-size: 18px;
  color: #777;
}
</style>
