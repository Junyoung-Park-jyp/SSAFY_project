// products.js
import axios from 'axios';
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import { useUserStore } from './users';

export const useProductStore = defineStore('product', () => {
  const router = useRouter();
  const deposits = ref([]);
  const savings = ref([]);
  const posts = ref([]);
  const userStore = useUserStore();
  const token = userStore.token;
  const isLogin = computed(() => !!token.value);

  const getDeposits = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/v1/products/depositproducts/');
      deposits.value = res.data;
    } catch (error) {
      console.error(error);
    }
  };

  const getSavings = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/v1/products/savingproducts/');
      savings.value = res.data;
    } catch (error) {
      console.error(error);
    }
  };

  const getPosts = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/v1/community/posts/');
      posts.value = res.data;
    } catch (error) {
      console.error(error);
    }
  };

  const getPostDetail = async (id) => {
    try {
      return await axios.get(`http://127.0.0.1:8000/api/v1/community/posts/${id}/`);
    } catch (error) {
      console.error(error);
    }
  };

  const toggleLike = async (postId) => {
    try {
      return await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/like/`, {}, {
        headers: { Authorization: `Token ${token.value}` }
      });
    } catch (error) {
      console.error(error);
    }
  };

  const addComment = async (postId, content) => {
    try {
      return await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/`, { content }, {
        headers: { Authorization: `Token ${token.value}` }
      });
    } catch (error) {
      console.error(error);
    }
  };

  const deleteComment = async (postId, commentId) => {
    try {
      return await axios.delete(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/${commentId}/`, {
        headers: { Authorization: `Token ${token.value}` }
      });
    } catch (error) {
      console.error(error);
    }
  };

  const toggleLikeComment = async (postId, commentId) => {
    try {
      return await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/${commentId}/like/`, {}, {
        headers: { Authorization: `Token ${token.value}` }
      });
    } catch (error) {
      console.error(error);
    }
  };

  return {
    deposits,
    savings,
    posts,
    getDeposits,
    getSavings,
    getPosts,
    getPostDetail,
    toggleLike,
    addComment,
    deleteComment,
    toggleLikeComment
  };
});
