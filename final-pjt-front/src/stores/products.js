import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useUserStore } from './users'

export const useProductStore = defineStore('product', () => {
  const router = useRouter()
  const deposits = ref([])
  const savings = ref([])
  const userStore = useUserStore()
  const token = userStore.token
  const isLogin = computed(() => !!token.value)

  const getDeposits = function () {
    axios.get('http://127.0.0.1:8000/api/v1/products/depositproducts/', {
      // headers: { Authorization: `Token ${token.value}` }
    })
    .then(res => deposits.value = res.data)
  }
  const getSavings = function () {
    axios.get('http://127.0.0.1:8000/api/v1/products/savingproducts/', {
      // headers: { Authorization: `Token ${token.value}` }
    })
    .then(res => savings.value = res.data)
  }

  const createProduct = function ({ title, content }) {
    axios.post('http://127.0.0.1:8000/api/v1/products/', { title, content }, {
      headers: { Authorization: `Token ${token.value}` }
    })
    .then((res) => {
      console.log(res)
      router.push({ name: 'home' })
    })
  }

  return { deposits, savings, getDeposits, getSavings, createProduct, token, isLogin }
}, { persist: true })
