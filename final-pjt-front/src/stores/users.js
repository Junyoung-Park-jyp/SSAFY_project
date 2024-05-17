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

  const SignUp = async (payload) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', payload)
      console.log('회원가입 완료', response.data)
      router.push({ name: 'login' })
    } catch (error) {
      console.error(error)
    }
  }

  const LogIn = async (payload) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/login/', payload)
      console.log('login', response.data)
      token.value = response.data.key
      router.push({ name: 'profile' })
    } catch (error) {
      console.error(error)
    }
  }

  const getProfile = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/accounts/profile/', {
        headers: { Authorization: `Token ${token.value}` }
      })
      return response.data
    } catch (error) {
      console.error(error)
      return null
    }
  }

  return { SignUp, LogIn, getProfile, token, isLogin }
}, { persist: true })
