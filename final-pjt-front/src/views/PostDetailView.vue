<template>
  <div class="container mt-4 post-detail">
    <div v-if="post" class="post-content">
      <div class="post-header">
        <h1>{{ post.title }}</h1>
        <div class="post-navigation">
          <button v-if="previousPost" @click="goToPost(previousPost)" class="nav-button">← 왼쪽 글</button>
          <button v-if="nextPost" @click="goToPost(nextPost)" class="nav-button">오른쪽 글 →</button>
        </div>
      </div>
      <div class="post-meta">
        <p>
          작성자: {{ post.author }}  |  작성일: {{ new Date(post.created_at).toLocaleString() }}  | 
          <button style="display: inline;" @click="toggleLikePost" class="like-button">
            <span :class="{ liked: likedByUser }">❤</span>
            {{ post.total_likes }}
          </button>
          <span v-if="post.author === user?.username" class="post-actions">
            <button @click="openEditPostModal" class="edit-button">수정</button>
            <button @click="deletePost" class="delete-button">삭제</button>
          </span>
        </p>
      </div>
      <h2>{{ post.content }}</h2>
      <br>
      <div class="comments-section">
        <h2>댓글 ({{ post.comments.length }})</h2>
        <ul>
          <li v-for="comment in post.comments" :key="comment.id" class="comment">
            <div class="comment-meta">
              <p>{{ comment.author }} ({{ new Date(comment.created_at).toLocaleString() }})
                <button style="display: inline;" @click="toggleLikeComment(comment)" class="like-button2">
                  <span :class="{ liked: comment.likedByUser }">❤</span>
                  {{ comment.total_likes }}
                </button>
              </p>
            </div>
            <p style="font-size: 20px;">{{ comment.content }}</p>
            <div class="comment-actions">
              <button v-if="comment.author === user?.username" @click="openEditCommentModal(comment)" class="edit-button">수정</button>
              <button v-if="comment.author === user?.username" @click="deleteComment(comment.id)" class="delete-button">삭제 </button> 
            </div>
          </li>
        </ul>
        <br>
        <div class="comment-form">
          <h3>댓글 작성</h3>
          <textarea v-model="newComment.content" placeholder="댓글을 입력하세요"></textarea>
          <button @click="addComment" class="btn btn-primary">댓글 작성</button>
          <button @click="goBack" class="btn btn-secondary">뒤로 가기</button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>

    <!-- Edit Comment Modal -->
    <div v-if="isEditCommentModalOpen" class="modal">
      <div class="modal-content">
        <h2>댓글 수정</h2>
        <textarea v-model="editCommentData.content" placeholder="내용을 입력하세요"></textarea>
        <button @click="editComment">저장</button>
        <button @click="closeEditCommentModal">취소</button>
      </div>
    </div>

    <!-- Edit Post Modal -->
    <div v-if="isEditPostModalOpen" class="modal">
      <div class="modal-content">
        <h2>게시글 수정</h2>
        <input v-model="editPostData.title" placeholder="제목을 입력하세요" />
        <textarea v-model="editPostData.content" placeholder="내용을 입력하세요"></textarea>
        <button @click="editPost">저장</button>
        <button @click="closeEditPostModal">취소</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { useProductStore } from '@/stores/products';
import { useUserStore } from '@/stores/users';
import { useRoute, useRouter } from 'vue-router';

export default {
  setup() {
    const post = ref(null);
    const previousPost = ref(null);
    const nextPost = ref(null);
    const newComment = ref({ content: '' });
    const productStore = useProductStore();
    const userStore = useUserStore();
    const user = ref(null);
    const route = useRoute();
    const router = useRouter();
    const likedByUser = ref(false);

    const isEditCommentModalOpen = ref(false);
    const editCommentData = ref({ id: null, content: '' });

    const isEditPostModalOpen = ref(false);
    const editPostData = ref({ title: '', content: '' });

    const fetchPost = async (postId) => {
      if (userStore.token) {
        user.value = await userStore.getProfile();
        try {
          const response = await productStore.getPostDetail(postId);
          post.value = response;
          likedByUser.value = post.value.likes.includes(user.value.id);
          post.value.comments.forEach((comment) => {
            comment.likedByUser = comment.likes.includes(user.value.id);
          });
          const navigation = await productStore.getPostNavigation(postId);
          previousPost.value = navigation.previous;
          nextPost.value = navigation.next;
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
        post.value.comments = post.value.comments.filter((comment) => comment.id !== commentId);
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
        const comment = post.value.comments.find((c) => c.id === editCommentData.value.id);
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

    const openEditPostModal = () => {
      editPostData.value = { title: post.value.title, content: post.value.content };
      isEditPostModalOpen.value = true;
    };

    const closeEditPostModal = () => {
      isEditPostModalOpen.value = false;
    };

    const editPost = async () => {
      const { postId } = route.params;
      try {
        const response = await productStore.editPost(postId, editPostData.value);
        post.value.title = response.title;
        post.value.content = response.content;
        closeEditPostModal();
      } catch (error) {
        console.error('Failed to edit post:', error);
      }
    };

    const deletePost = async () => {
      const { postId } = route.params;
      try {
        await productStore.deletePost(postId);
        router.push({ name: 'community' });
      } catch (error) {
        console.error('Failed to delete post:', error);
      }
    };

    const goBack = () => {
      router.push({ name: 'community' });
    };

    const goToPost = (postId) => {
      router.push({ name: 'post', params: { postId } });
    };

    watch(route, (newRoute) => {
      fetchPost(newRoute.params.postId);
    });

    onMounted(() => {
      fetchPost(route.params.postId);
    });

    return {
      post,
      previousPost,
      nextPost,
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
      goToPost,
      openEditPostModal,
      closeEditPostModal,
      isEditPostModalOpen,
      editPostData,
      editPost,
      deletePost,
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
  background: linear-gradient(to right, #f0f4f8, #d9e2ec);
  color: #333;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container {
  max-width: 900px;
  margin: 20px auto;
  padding: 20px;
}

.post-detail {
  background: linear-gradient(to bottom right, #ffffff, #e6f7ff);
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  font-family: 'Montserrat', sans-serif;
  color: #333;
  transition: transform 0.3s, box-shadow 0.3s;
  animation: fadeIn 0.5s ease-in-out;
  width: 100%;
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

.post-detail:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.post-header h1 {
  font-size: 36px;
  color: #005c99;
  margin-bottom: 20px;
  border-bottom: 3px solid #005c99;
  padding-bottom: 10px;
  animation: slideIn 0.5s ease-in-out;
}

@keyframes slideIn {
  from {
    transform: translateX(-20px);
  }
  to {
    transform: translateX(0);
  }
}

.post-navigation {
  display: flex;
  align-items: center;
}

.nav-button {
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 10px;
  margin: 0 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.nav-button:hover {
  background-color: #004080;
  transform: translateY(-2px);
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.post-meta p {
  font-size: 15px;
  color: #555;
  margin-top: 0;
  margin-bottom: 40px;
}

.like-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #ff4d4d;
  font-size: 17px;
  transition: transform 0.3s ease, color 0.3s ease;
  display: flex;
  align-items: center;
}

.like-button2 {
  background: none;
  border: none;
  cursor: pointer;
  color: #ff4d4d;
  font-size: 15px;
  transition: transform 0.3s ease, color 0.3s ease;
  display: flex;
  align-items: center;
}

.like-button span,
.like-button2 span {
  margin-right: 8px;
}

.like-button:hover,
.like-button2:hover {
  transform: scale(1.2);
  color: #e60000;
}

.liked {
  color: #e60000;
}

.edit-button,
.delete-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #005c99;
  font-size: 13px;
  margin-left: 0px;
  transition: color 0.3s ease;
}

.edit-button:hover,
.delete-button:hover {
  color: #004080;
}

.comments-section {
  margin-top: 40px;
}

.comments-section h2 {
  color: #005c99;
  font-size: 24px;
  margin-bottom: 20px;
  border-bottom: 3px solid #005c99;
  padding-bottom: 10px;
}

.comment {
  border-bottom: 1px solid #ddd;
  padding: 15px 0;
  margin-bottom: 15px;
  border-radius: 10px;
  background: #f9f9f9;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.comment:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.comment-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comment-meta p {
  font-size: 14px;
  color: #333;
  margin-bottom: 10px;
}

.comment-actions {
  display: flex;
  align-items: center;
}

.comment-actions .like-button,
.comment-actions .edit-button,
.comment-actions .delete-button {
  margin-right: 5px;
}

.comment-form {
  margin-top: 20px;
  animation: fadeInUp 0.5s ease-in-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.comment-form h3 {
  color: #005c99;
  font-size: 20px;
  margin-bottom: 10px;
}

.comment-form textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-bottom: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.comment-form textarea:focus {
  border-color: #005c99;
  box-shadow: 0 0 10px rgba(0, 92, 153, 0.2);
}

.comment-form button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #005c99;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.comment-form button:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  margin-top: 20px;
  margin-right: 20px;
}

.btn-primary:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}

.btn-secondary {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #999, #bbe1fa);
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  margin-top: 20px;
}

.btn-secondary:hover {
  background-color: #999;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
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
  transition: opacity 0.3s;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 15px;
  width: 400px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transform: scale(0.9);
  transition: transform 0.3s, box-shadow 0.3s;
}

.modal-content:hover {
  transform: scale(1);
  box-shadow: 0 15px 45px rgba(0, 0, 0, 0.3);
}

.modal h2 {
  margin-top: 0;
  color: #005c99;
}

.modal textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.modal textarea:focus {
  border-color: #005c99;
  box-shadow: 0 0 10px rgba(0, 92, 153, 0.2);
}

.modal button {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
}

.modal button:first-of-type {
  background-color: #005c99;
  color: white;
}

.modal button:first-of-type:hover {
  background-color: #004080;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.modal button:last-of-type {
  background-color: #ccc;
  color: white;
  margin-left: 0px;
}

.modal button:last-of-type:hover {
  background-color: #999;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
