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
    const age = payload.age
    const bank = payload.bank
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/signup/`,
      data : {
        username, password1, password2, age, bank
      }
    })
    .then((res) => {
      LogIn({username, password})
      router.push({ name: 'home' })
    })
    .catch(err => console.log(err))
  }

  const UserInfo = function(payload){
    const age = payload.age
    const current_balance = payload.current_balance
    const bank = payload.bank
    const annual_salary = payload.annual_salary
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/userinfo/',
      data: {
        age, current_balance, bank, annual_salary
      }
    })
  }

  const UserInfo = function(payload){
    const age = payload.age
    const current_balance = payload.current_balance
    const bank = payload.bank
    const annual_salary = payload.annual_salary
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/userinfo/',
      data: {
        age, current_balance, bank, annual_salary
      }
    })
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

  return { SignUp, UserInfo, LogIn, getProfile, token, isLogin }
}, { persist: true })
