import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import LogInView from '../views/LogInView.vue'
import SignUpView from '../views/SignUpView.vue'
import { useArticleStore } from '@/stores/articles'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },    
  ]
})

router.beforeEach((to, from) => {
  const store = useArticleStore()
  if (to.name === 'home' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  }
  if ((to.name === 'signup' || to.name === 'login') && (store.isLogin)) {
    window.alert('이미 로그인한 사용자입니다.')
    return { name: 'home' }
  }
})

export default router
