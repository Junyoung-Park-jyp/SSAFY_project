<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button @click="router.push({name: 'create'})">게시글 생성</button>
    <BankSearchForm />
    <ProductList />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import BankSearchForm from '../components/BankSearchForm.vue';
import ProductList from '../components/ProductList.vue';

const router = useRouter()
</script>

<style scoped>
/* Add styles specific to this component */
</style>
