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
          <button v-if="comment.author === user?.username" @click="deleteComment(comment.id)" class="delete-button">삭제</button>
          <button v-if="comment.author === user?.username" @click="openEditCommentModal(comment)" class="edit-button">수정</button>
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

    <!-- Edit Comment Modal -->
    <div v-if="isEditCommentModalOpen" class="modal">
      <div class="modal-content">
        <h2>댓글 수정</h2>
        <textarea v-model="editCommentData.content" placeholder="내용을 입력하세요"></textarea>
        <button @click="editComment">저장</button>
        <button @click="closeEditCommentModal">취소</button>
      </div>
    </div>
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
    const user = ref(null);
    const route = useRoute();
    const router = useRouter();
    const likedByUser = ref(false);

    const isEditCommentModalOpen = ref(false);
    const editCommentData = ref({ id: null, content: '' });

    const fetchPost = async () => {
      const { postId } = route.params;
      if (userStore.token) {
        user.value = await userStore.getProfile();
        try {
          const response = await productStore.getPostDetail(postId);
          post.value = response;
          likedByUser.value = post.value.likes.includes(user.value.id);
          post.value.comments.forEach(comment => {
            comment.likedByUser = comment.likes.includes(user.value.id);
          });
        } catch (error) {
          console.error('Failed to fetch post:', error);
        }
      } else {
        console.error('User is not authenticated');
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

    const openEditCommentModal = (comment) => {
      editCommentData.value = { id: comment.id, content: comment.content };
      isEditCommentModalOpen.value = true;
    };

    const closeEditCommentModal = () => {
      isEditCommentModalOpen.value = false;
    };

    const editComment = async () => {
      const { postId } = route.params;
      try {
        const response = await productStore.editComment(postId, editCommentData.value.id, editCommentData.value);
        const comment = post.value.comments.find(c => c.id === editCommentData.value.id);
        comment.content = response.content;
        closeEditCommentModal();
      } catch (error) {
        console.error('Failed to edit comment:', error);
      }
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
      openEditCommentModal,
      closeEditCommentModal,
      editCommentData,
      isEditCommentModalOpen,
      editComment,
      toggleLikeComment,
      goBack,
    };
  },
};
</script>

<style scoped>
.post-detail {
  background: #ffffff;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

.post-detail h1 {
  font-size: 32px;
  color: #005c99;
  margin-bottom: 20px;
  border-bottom: 2px solid #005c99;
  padding-bottom: 10px;
}

.post-detail p {
  font-size: 18px;
  color: #555;
  margin-bottom: 20px;
  line-height: 1.6;
}

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #ff4d4d;
  font-size: 24px;
  transition: transform 0.3s ease, color 0.3s ease;
}

.like-button:hover {
  transform: scale(1.2);
  color: #e60000;
}

.liked {
  color: #e60000;
}

.edit-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #005c99;
  font-size: 16px;
  margin-left: 10px;
  transition: color 0.3s ease;
}

.edit-button:hover {
  color: #004080;
}

.comments-section {
  margin-top: 40px;
}

.comments-section h2 {
  color: #005c99;
  font-size: 24px;
  margin-bottom: 20px;
  border-bottom: 2px solid #005c99;
  padding-bottom: 10px;
}

.comment {
  border-bottom: 1px solid #ddd;
  padding: 15px 0;
  margin-bottom: 15px;
}

.comment p {
  font-size: 16px;
  color: #333;
  margin-bottom: 10px;
}

.comment-meta {
  color: #999;
  margin-bottom: 10px;
}

.comment-actions {
  display: flex;
  align-items: center;
}

.comment-actions .like-button,
.comment-actions .edit-button,
.comment-actions .delete-button {
  margin-right: 10px;
}

.comment-form {
  margin-top: 20px;
}

.comment-form textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.comment-form textarea:focus {
  border-color: #005c99;
}

.comment-form .btn-primary {
  width: 100%;
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
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.btn-secondary {
  display: inline-block;
  padding: 12px 24px;
  background-color: #ccc;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  margin-top: 20px;
}

.btn-secondary:hover {
  background-color: #999;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 15px;
  width: 400px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.modal h2 {
  margin-top: 0;
  color: #005c99;
}

.modal input,
.modal textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.modal input:focus,
.modal textarea:focus {
  border-color: #005c99;
}
</style>

