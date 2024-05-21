<template>
  <div v-if="post" class="container post-detail">
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>작성자: {{ post.author }} | 작성일: {{ new Date(post.created_at).toLocaleString() }}</p>
    <button @click="toggleLikePost" class="like-button">
      <span :class="{ liked: likedByUser }">❤</span>
      {{ post.total_likes }}
    </button>
    <div class="comments-section">
      <h2>댓글 ({{ post.comments.length }})</h2>
      <ul>
        <li v-for="comment in post.comments" :key="comment.id" class="comment">
          <p>{{ comment.content }}</p>
          <p>작성자: {{ comment.author }} | 작성일: {{ new Date(comment.created_at).toLocaleString() }}</p>
          <button v-if="comment.author === user.username" @click="deleteComment(comment.id)" class="delete-button">삭제</button>
          <button v-if="comment.author === user.username" @click="editComment(comment)" class="edit-button">수정</button>
          <button @click="toggleLikeComment(comment)" class="like-button">
            <span :class="{ liked: comment.likedByUser }">❤</span>
            {{ comment.total_likes }}
          </button>
        </li>
      </ul>
      <div class="comment-form">
        <h3>댓글 작성</h3>
        <textarea v-model="newComment.content" placeholder="댓글을 입력하세요"></textarea>
        <button @click="addComment">댓글 작성</button>
      </div>
    </div>
    <button @click="goBack" class="btn btn-secondary">뒤로 가기</button>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/products';
import { useUserStore } from '@/stores/users';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const post = ref(null);
    const newComment = ref({ content: '' });
    const productStore = useProductStore();
    const userStore = useUserStore();
    const user = userStore.user;
    const route = useRoute();
    const router = useRouter();
    const likedByUser = ref(false);

    const fetchPost = async () => {
      const { postId } = route.params;
      try {
        const response = await productStore.getPostDetail(postId);
        post.value = response;
        likedByUser.value = post.value.likes.includes(user.id);
        post.value.comments.forEach(comment => {
          comment.likedByUser = comment.likes.includes(user.id);
        });
      } catch (error) {
        console.error('Failed to fetch post:', error);
      }
    };

    const toggleLikePost = async () => {
      const { postId } = route.params;
      try {
        const response = await productStore.toggleLikePost(postId);
        post.value.total_likes = response.total_likes;
        likedByUser.value = !likedByUser.value;
      } catch (error) {
        console.error('Failed to like post:', error);
      }
    };

    const addComment = async () => {
      const { postId } = route.params;
      try {
        const response = await productStore.addComment(postId, newComment.value);
        post.value.comments.push(response);
        newComment.value.content = '';
      } catch (error) {
        console.error('Failed to add comment:', error);
      }
    };

    const deleteComment = async (commentId) => {
      const { postId } = route.params;
      try {
        await productStore.deleteComment(postId, commentId);
        post.value.comments = post.value.comments.filter(comment => comment.id !== commentId);
      } catch (error) {
        console.error('Failed to delete comment:', error);
      }
    };

    const editComment = (comment) => {
      // 수정 로직을 여기에 추가하세요.
    };

    const toggleLikeComment = async (comment) => {
      const { postId } = route.params;
      try {
        const response = await productStore.toggleLikeComment(postId, comment.id);
        comment.total_likes = response.total_likes;
        comment.likedByUser = !comment.likedByUser;
      } catch (error) {
        console.error('Failed to like comment:', error);
      }
    };

    const goBack = () => {
      router.go(-1);
    };

    onMounted(fetchPost);

    return {
      post,
      newComment,
      user,
      likedByUser,
      toggleLikePost,
      addComment,
      deleteComment,
      editComment,
      toggleLikeComment,
      goBack,
    };
  },
};
</script>

<style scoped>
.post-detail {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #ff0000;
  font-size: 24px;
}

.liked {
  color: #ff0000;
}

.comments-section {
  margin-top: 20px;
}

.comment-form {
  margin-top: 20px;
}

.comment {
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.comment .like-button {
  font-size: 18px;
}

.comment .delete-button,
.comment .edit-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #005c99;
  font-size: 14px;
  margin-left: 10px;
}
</style>
