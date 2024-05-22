import axios from 'axios';
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore('user', () => {
  const router = useRouter();
  const token = ref(localStorage.getItem('token') || null);
  const isLogin = computed(() => !!token.value);
  const user = ref(null);
  const errorMessage = ref('');

  const SignUp = async (payload) => {
    const { username, password1, password2, email } = payload;
    try {
      await axios.post('http://127.0.0.1:8000/accounts/signup/', { username, password1, password2, email });
      await LogIn({ username, password: password1 });
      router.push({ name: 'userinfo', params: { username } });
    } catch (err) {
      errorMessage.value = 'Signup failed. Please try again.';
      console.error(err);
    }
  };

  const UserInfo = async (payload) => {
    const { username, age, current_balance, bank, annual_salary } = payload;
    try {
      await axios.post('http://127.0.0.1:8000/api/v1/accounts/userinfo/', { username, age, current_balance, bank, annual_salary }, {
        headers: { Authorization: `Token ${token.value}` }
      });
      router.push({ name: 'home' });
    } catch (err) {
      console.error(err);
    }
  };

  const LogIn = async (payload) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/login/', payload);
      token.value = response.data.key;
      localStorage.setItem('token', token.value);
      user.value = await getProfile();
      errorMessage.value = '';  // Reset error message on successful login
      router.push({ name: 'home' });
    } catch (err) {
      errorMessage.value = 'Invalid username or password.';
      console.error(err);
    }
  };

  const LogOut = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/accounts/logout/', {}, {
        headers: { Authorization: `Token ${token.value}` }
      });
      token.value = null;
      user.value = null;
      localStorage.removeItem('token');
      router.push({ name: 'login' });
    } catch (err) {
      console.error(err);
    }
  };

  const getProfile = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/accounts/profile/', {
        headers: { Authorization: `Token ${token.value}` }
      });
      return response.data;
    } catch (error) {
      console.error(error);
      return null;
    }
  };

  return { SignUp, UserInfo, LogIn, LogOut, getProfile, token, isLogin, user, errorMessage };
}, { persist: true });
