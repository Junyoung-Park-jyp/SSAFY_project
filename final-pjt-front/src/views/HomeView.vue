<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <DepositList />
    <SavingList />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import DepositList from '../components/DepositList.vue';
import SavingList from '../components/SavingList.vue';
const router = useRouter()
</script>

<style lang="scss" scoped>

</style>