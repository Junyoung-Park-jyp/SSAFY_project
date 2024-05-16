<template>
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {{ userStore.user.username }}!</p>
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
  