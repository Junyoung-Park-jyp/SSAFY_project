import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()
  const articles = ref([])
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
      console.log('회원가입 완료')
      router.push({ name: 'home' })
    })
    .catch(err => console.log(err))
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
  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {console.log(res)
      router.push({name: 'home'})
    })
  }

  return { articles, getArticles, createArticle, SignUp, LogIn, token, isLogin }
}, { persist: true })
