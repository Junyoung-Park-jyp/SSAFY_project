import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProductCreateView from '../views/ProductCreateView.vue';
import LogInView from '../views/LogInView.vue';
import SignUpView from '../views/SignUpView.vue';
import ProfileView from '../views/ProfileView.vue';
import ProductView from '../views/ProductView.vue';
import DepositView from '../views/DepositView.vue';
import DepositDetailView from '../views/DepositDetailView.vue';
import SavingView from '../views/SavingView.vue';
import SavingDetailView from '../views/SavingDetailView.vue';
import CommunityView from '../views/CommunityView.vue';
import CommunityCreateView from '../views/CommunityCreateView.vue';
import ExchangeRateCalculator from '../views/ExchangeRateCalculator.vue';
import ErrorView from '../views/ErrorView.vue';
import UserInfoView from '../views/UserInfoView.vue';
import PostDetailView from '../views/PostDetailView.vue';
import KakaoMapView from '../views/KakaoMapView.vue';
import ChatbotView from '../views/ChatbotView.vue'; // 추가된 부분
import BankClerkView from '../views/BankClerkView.vue'; // 추가된 부분
import { useUserStore } from '@/stores/users';
import { useProductStore } from '@/stores/products';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/accounts',
    children: [
      {
        path: '',
        name: 'accounts',
      },
      {
        path: 'signup',
        name: 'signup',
        component: SignUpView
      },
      {
        path: 'login',
        name: 'login',
        component: LogInView
      },
      {
        path: 'profile',
        name: 'profile',
        component: ProfileView
      },
      {
        path: 'userinfo/:username',
        name: 'userinfo',
        component: UserInfoView
      }
    ]
  },
  {
    path: '/create',
    name: 'create',
    component: CommunityCreateView
  },
  {
    path: '/community',
    children: [
      {
        path: '',
        name: 'community',
        component: CommunityView
      },
      {
        path: ':postId',
        name: 'post',
        component: PostDetailView
      }
    ]
  },
  {
    path: '/products',
    name: 'products',
    component: ProductView,
    children: [
      {
        path: 'deposit',
        name: 'deposit',
        component: DepositView
      },
      {
        path: 'saving',
        name: 'saving',
        component: SavingView
      }
    ]
  },
  {
    path: '/deposit/:id',
    name: 'depositDetail',
    component: DepositDetailView
  },
  {
    path: '/saving/:id',
    name: 'savingDetail',
    component: SavingDetailView
  },
  {
    path: '/exchange-rate-calculator',
    name: 'exchangeRateCalculator',
    component: ExchangeRateCalculator
  },
  {
    path: '/error/:code',
    name: 'error',
    component: ErrorView
  },
  {
    path: '/search',
    name: 'search',
    component: KakaoMapView
  },
  {
    path: '/chatbot',
    name: 'chatbot',
    component: ChatbotView
  },
  {
    path: '/bankclerk',
    name: 'bankclerk',
    component: BankClerkView
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from) => {
  const userStore = useUserStore();
  const productStore = useProductStore();
  
  if (to.name === 'create' && !userStore.isLogin) {
    window.alert('로그인이 필요합니다.');
    return { name: 'login' };
  }
  
  if (to.name === 'profile' && !userStore.isLogin) {
    window.alert('로그인이 필요합니다.');
    return { name: 'login' };
  }
  
  if (to.name === 'community' && !userStore.isLogin) {
    window.alert('로그인이 필요합니다.');
    return { name: 'login' };
  }

  if ((to.name === 'signup' || to.name === 'login') && (userStore.isLogin)) {
    window.alert('이미 로그인한 사용자입니다.');
    return { name: 'home' };
  }
});

export default router;
