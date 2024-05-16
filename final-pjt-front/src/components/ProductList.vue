<template>
    <div>
      <h2>제품 목록</h2>
      {{ products }}
      <ul>
        <!-- <li v-for="product in products" :key="product.id">
          <h3>{{ product.title }}</h3>
          <p>{{ product.content }}</p>
        </li> -->
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useProductStore } from '@/stores/products';
  import { storeToRefs } from 'pinia';
  
  const store = useProductStore()
  const { products } = storeToRefs(store)
  
  onMounted(() => {
    store.getProducts()
  })
  </script>
  
  <style scoped>
  /* Add styles specific to this component */
  </style>
  