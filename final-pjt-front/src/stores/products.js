import axios from 'axios';
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import { useUserStore } from './users';

export const useProductStore = defineStore('product', () => {
  const router = useRouter();
  const deposits = ref([]);
  const savings = ref([]);
  const userStore = useUserStore();
  const token = userStore.token;
  const isLogin = computed(() => !!token.value);

  const getDeposits = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/v1/products/depositproducts/');
      deposits.value = res.data;
      // console.log('Deposits:', deposits.value); // 데이터 로드 확인
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
  const createCommunity = function ({ title, content }) {
    axios.post('http://127.0.0.1:8000/api/v1/products/', { title, content }, {
      headers: { Authorization: `Token ${token.value}` }
    })
    .then((res) => {
      console.log(res)
      router.push({ name: 'home' })
    })
  }

  return { deposits, savings, getDeposits, getSavings, createCommunity, token, isLogin }
}, { persist: true })
