import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import Dashboard from './views/Dashboard.vue';
import ProductList from './views/ProductList.vue';
import ProductDetail from './views/ProductDetail.vue';
import ExchangeCalculator from './views/ExchangeCalculator.vue';
import BankSearch from './views/BankSearch.vue';
import Community from './views/Community.vue';
import Profile from './views/Profile.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/dashboard', component: Dashboard },
  { path: '/products', component: ProductList },
  { path: '/products/:id', component: ProductDetail },
  { path: '/exchange', component: ExchangeCalculator },
  { path: '/banks', component: BankSearch },
  { path: '/community', component: Community },
  { path: '/profile', component: Profile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
