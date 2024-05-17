import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const token = ref(null)
  const isLogin = computed(() => {
    return token.value !== null
  })

  const SignUp = function(payload) {
    const { username, password1, password2 } = payload
    axios.post('http://127.0.0.1:8000/accounts/signup/', {
      username, password1, password2
    })
    .then(res => {
      console.log('회원가입 완료')
      router.push({ name: 'home' })
    })
    .catch(err => {
      if (err.response) {
        console.log('Response data:', err.response.data)
        console.log('Response status:', err.response.status)
        console.log('Response headers:', err.response.headers)
      } else if (err.request) {
        console.log('Request data:', err.request)
      } else {
        console.log('Error message:', err.message)
      }
      console.log('Error config:', err.config)
    })
  }

  const LogIn = function(payload) {
    const { username, password } = payload
    axios.post('http://127.0.0.1:8000/accounts/login/', {
      username, password
    })
    .then(res => {
      console.log('login')
      token.value = res.data.key
      router.push({ name: 'home' })
    })
    .catch(err => {
      if (err.response) {
        console.log('Response data:', err.response.data)
        console.log('Response status:', err.response.status)
        console.log('Response headers:', err.response.headers)
      } else if (err.request) {
        console.log('Request data:', err.request)
      } else {
        console.log('Error message:', err.message)
      }
      console.log('Error config:', err.config)
    })
  }

  const getProfile = function(payload) {
    const { username } = payload
    axios.get(`http://127.0.0.1:8000/accounts/profile/${username}`)
    .then(res => {
      console.log(res.data)
    })
    .catch(err => {
      if (err.response) {
        console.log('Response data:', err.response.data)
        console.log('Response status:', err.response.status)
        console.log('Response headers:', err.response.headers)
      } else if (err.request) {
        console.log('Request data:', err.request)
      } else {
        console.log('Error message:', err.message)
      }
      console.log('Error config:', err.config)
    })
  }

  return { SignUp, LogIn, getProfile, token, isLogin }
}, { persist: true })
