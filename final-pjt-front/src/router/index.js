import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductCreateView from '../views/ProductCreateView.vue'
import LogInView from '../views/LogInView.vue'
import SignUpView from '../views/SignUpView.vue'
import ProfileView from '../views/ProfileView.vue'
import ProductView from '../views/ProductView.vue'
import DepositView from '../views/DepositView.vue'
import DepositDetailView from '../views/DepositDetailView.vue'
import SavingView from '../views/SavingView.vue'
import SavingDetailView from '../views/SavingDetailView.vue'
import CommunityView from '../views/CommunityView.vue'
import { useUserStore } from '@/stores/users'
import { useProductStore } from '@/stores/products'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/accounts',
      children: [
        {
          path: '/',
          name: 'accounts',
        },
        {
          path: '/accounts/signup',
          name: 'signup',
          component: SignUpView
        },
        {
          path: '/accounts'
        },
        {
          path: '/accounts/login',
          name: 'login',
          component: LogInView
        },
        {
          path: '/accounts/profile',
          name: 'profile',
          component: ProfileView
        }
      ]
    },
    {
      path: '/create',
      name: 'create',
      component: ProductCreateView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductView,
      children: [
        {
          path: '/deposit',
          name: 'deposit',
          component: DepositView,
          children: [
            {
              path: '/:id',
              name: 'depositDetail',
              component: DepositDetailView
            }
          ]
        },
        {
          path: '/saving',
          name: 'saving',
          component: SavingView,
          childeren: [
            {
              path: '/:id',
              name: 'savingDetail',
              component: SavingDetailView
            }
          ]
        }
      ]
    }
  ]
})

router.beforeEach((to, from) => {
  const userStore = useUserStore()
  const productStore = useProductStore()
  if (to.name === 'home' && !userStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  }
  if ((to.name === 'signup' || to.name === 'login') && (userStore.isLogin)) {
    window.alert('이미 로그인한 사용자입니다.')
    return { name: 'home' }
  }
})

export default router
