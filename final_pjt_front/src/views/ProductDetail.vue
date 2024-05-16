<template>
    <div v-if="product">
      <h1>{{ product.name }}</h1>
      <p>{{ product.description }}</p>
      <p>Bank: {{ product.bank }}</p>
      <p>Interest Rate: {{ product.interest_rate }}%</p>
      <p>Duration: {{ product.duration_months }} months</p>
      <button @click="subscribe">Subscribe</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        product: null,
      };
    },
    async created() {
      const response = await axios.get(`http://localhost:8000/api/products/${this.$route.params.id}/`);
      this.product = response.data;
    },
    methods: {
      async subscribe() {
        // Add product subscription logic here
      }
    }
  };
  </script>
  