<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username</label>
        <input id="username" v-model="username" type="text" />
      </div>
      <div>
        <label for="email">Email</label>
        <input id="email" v-model="email" type="email" />
      </div>
      <div>
        <label for="password1">Password</label>
        <input id="password1" v-model="password1" type="password" />
      </div>
      <div>
        <label for="password2">Confirm Password</label>
        <input id="password2" v-model="password2" type="password" />
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import { useUserStore } from '../store/user';

export default {
  data() {
    return {
      username: '',
      email: '',
      password1: '',
      password2: '',
    };
  },
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },
  methods: {
    async register() {
      await this.userStore.register({
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      });
      this.$router.push('/login');
    },
  },
};
</script>
