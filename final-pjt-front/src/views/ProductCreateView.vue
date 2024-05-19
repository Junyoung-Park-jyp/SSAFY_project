<template>
  <div>
    <h1>제품 생성 페이지</h1>
    <form @submit.prevent="createProduct">
      <label for="title">제목:</label>
      <input type="text" id="title" v-model.trim="title">
      <label for="content">내용:</label>
      <textarea id="content" v-model.trim="content"></textarea>
      <input type="submit" value="생성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProductStore } from '@/stores/products';

const title = ref('')
const content = ref('')
const store = useProductStore()

const createProduct = () => {
  const payload = {
    title: title.value,
    content: content.value
  }
  store.createProduct(payload)
}
</script>

<style scoped>
/* Add styles specific to this component */
</style>
