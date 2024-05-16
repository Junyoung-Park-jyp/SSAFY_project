<template>
    <div>
      <h1>Profile</h1>
      <div v-if="userStore.user">
        <p>Username: {{ userStore.user.username }}</p>
        <p>Email: {{ userStore.user.email }}</p>
        <p>Subscribed Products: {{ userStore.user.subscribed_products }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { useUserStore } from '../store/user';
  
  export default {
    setup() {
      const userStore = useUserStore();
      return { userStore };
    }
  };
  </script>
  