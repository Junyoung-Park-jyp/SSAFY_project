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

  const LogIn = function(payload){
    const username = payload.username
    const password = payload.password
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data : {
        username, password
      }
    })
    .then((res)=> {
      console.log('login')
      token.value = res.data.key
      router.push({ name: 'home' })
    })
    .catch(err => console.log(err))
  }

  const getProfile = function(payload){
    const username = payload.username

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${username}`,
    })
    .then((res) => {
      console.log(res.data)
    })
    .catch(err => console.log(err))
  }

  return { SignUp, UserInfo, LogIn, getProfile, token, isLogin }
}, { persist: true })
