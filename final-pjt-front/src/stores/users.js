import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const SignUp = function(payload){
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/signup/`,
      data : {
        username, password1, password2
      }
    })
    .then((res) => {
      LogIn({ username:username, password:password1 })
      router.push({ name: 'userinfo', params:{ username: username}})
    })
    .catch(err => router.push({ name: 'error', params: { code: err}}))
  }

  const UserInfo = function(payload){
    const username = payload.username
    const age = payload.age
    const current_balance = payload.current_balance
    const bank = payload.bank
    const annual_salary = payload.annual_salary
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/accounts/userinfo/',
      data: {
        username, age, current_balance, bank, annual_salary
      },
      headers: { Authorization: `Token ${token.value}` }
      
    })
  }

  const LogIn = async (payload) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/accounts/login/', payload)
      console.log('login', response.data)
      token.value = response.data.key
      // router.push({ name: 'profile' })
    } catch (err) {
      router.push({ name: 'error', params: { code: err}})
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

  return { SignUp, UserInfo, LogIn, getProfile, token, isLogin }
}, { persist: true })
