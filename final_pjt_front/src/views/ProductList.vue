<template>
    <div>
      <h1>Products</h1>
      <div v-for="product in products" :key="product.id">
        <router-link :to="'/products/' + product.id">
          {{ product.name }} ({{ product.bank }})
        </router-link>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        products: [],
      };
    },
    async created() {
      const response = await axios.get('http://localhost:8000/api/products/');
      this.products = response.data;
    }
  };
  </script>
  