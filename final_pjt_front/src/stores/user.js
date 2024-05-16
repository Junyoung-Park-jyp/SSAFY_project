import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: null,
  }),
  actions: {
    async login(credentials) {
      const response = await axios.post('http://localhost:8000/api/auth/login/', credentials);
      this.token = response.data.key;
      this.fetchUser();
    },
    async fetchUser() {
      const response = await axios.get('http://localhost:8000/api/auth/user/', {
        headers: {
          Authorization: `Token ${this.token}`
        }
      });
      this.user = response.data;
    },
    logout() {
      this.user = null;
      this.token = null;
    }
  }
});
