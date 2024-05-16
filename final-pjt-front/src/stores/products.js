import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useProductStore = defineStore('product', () => {
  const router = useRouter()
  const products = ref([])
  const token = ref(localStorage.getItem('token'))
  
  const isLogin = computed(() => !!token.value)

  const SignUp = function(payload){
    const { username, password1, password2 } = payload
    axios.post('http://127.0.0.1:8000/accounts/signup/', { username, password1, password2 })
      .then((res) => {
        console.log('회원가입 완료')
        router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
  }

  const LogIn = function(payload){
    const { username, password } = payload
    axios.post('http://127.0.0.1:8000/accounts/login/', { username, password })
      .then((res)=> {
        console.log('login')
        token.value = res.data.key
        localStorage.setItem('token', res.data.key)
        router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
  }

  const getProducts = function () {
    axios.get('http://127.0.0.1:8000/api/v1/products/depositproducts/', {
      // headers: { Authorization: `Token ${token.value}` }
    })
    .then(res => products.value = res.data)
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

  return { products, getProducts, createProduct, SignUp, LogIn, token, isLogin }
}, { persist: true })
