<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username</label>
        <input id="username" v-model="username" type="text" />
      </div>
      <div>
        <label for="password">Password</label>
        <input id="password" v-model="password" type="password" />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { useUserStore } from '../store/user';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },
  methods: {
    async login() {
      await this.userStore.login({
        username: this.username,
        password: this.password,
      });
      this.$router.push('/dashboard');
    },
  },
};
</script>
