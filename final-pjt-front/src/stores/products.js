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
  const token = computed(() => userStore.token);
  const isLogin = computed(() => !!token.value);

  const getAuthHeaders = () => {
    return {
      headers: {
        Authorization: `Token ${token.value}`
      }
    };
  };

  const getPostDetail = async (postId) => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/`, getAuthHeaders());
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const toggleLikePost = async (postId) => {
    try {
      const res = await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/like/`, {}, getAuthHeaders());
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const addComment = async (postId, commentData) => {
    try {
      const res = await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/`, commentData, getAuthHeaders());
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const deleteComment = async (postId, commentId) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/${commentId}/`, getAuthHeaders());
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const editComment = async (postId, commentId, commentData) => {
    try {
      const res = await axios.put(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/${commentId}/`, commentData, getAuthHeaders());
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

  const toggleLikeComment = async (postId, commentId) => {
    try {
      const res = await axios.post(`http://127.0.0.1:8000/api/v1/community/posts/${postId}/comments/${commentId}/like/`, {}, getAuthHeaders());
      return res.data;
    } catch (error) {
      console.error(error);
      throw error;
    }
  };

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

  const createCommunity = async ({ title, content }) => {
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/v1/community/posts/', { title, content }, getAuthHeaders());
      console.log(res);
      router.push({ name: 'home' });
    } catch (error) {
      console.error(error);
    }
  };

  return {
    deposits,
    savings,
    getDeposits,
    getSavings,
    createCommunity,
    getPostDetail,
    toggleLikePost,
    addComment,
    deleteComment,
    editComment,
    toggleLikeComment,
    token,
    isLogin
  };
}, { persist: true });
