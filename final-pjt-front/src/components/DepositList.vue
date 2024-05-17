<template>
  <div>
    <ul>
      <div
        v-for="deposit in store.deposits"
        :key="deposit.id"
      >
        
        <p>제목 : {{ deposit.etc_note }}</p>
        <!-- <p>내용 : {{ article.content }}</p> -->
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useProductStore } from '@/stores/products'
const store = useProductStore()
console.log(store.deposits)
console.log(store.savings)

</script>

<style scoped>

</style>