<template>
  <div class="community-container">
    <h1>커뮤니티 게시판</h1>
    <RouterLink :to="{ name: 'create' }" class="btn btn-primary">게시글 작성</RouterLink>
    <div v-if="posts.length" class="post-list">
      <h2>게시물 목록</h2>
      <ul>
        <li v-for="post in posts" :key="post.id" class="post-item">
          <RouterLink :to="{ name: 'post', params: { postId: post.id }}" class="post-link">
            {{ post.title }} 좋아요 {{ post.total_likes }}
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
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.btn-primary {
  padding: 10px 20px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #004080;
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
