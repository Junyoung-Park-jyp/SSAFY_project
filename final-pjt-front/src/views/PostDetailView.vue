<template>
  <div>
    <h1>{{ postId }}번 게시물</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
const route = useRoute()

const postId = route.params.postId 
</script>
<style scoped>

</style>