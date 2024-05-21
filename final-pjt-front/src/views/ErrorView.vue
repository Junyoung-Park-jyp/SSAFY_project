<template>
  <div>
    <h1>{{ error }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
const error = route.params.code
</script>

<style scoped>

</style>