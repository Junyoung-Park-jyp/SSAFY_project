<template>
  <div>
    <header>
      <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
          <RouterLink class="navbar-brand" to="/">
            <img src="@/assets/logo.png" alt="Bank For You Logo" class="nav-logo" style="border-radius: 50%;">
            Bank For You
          </RouterLink>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item" v-if="!isLogin">
                <RouterLink class="nav-link" :to="{name: 'signup'}">Sign Up</RouterLink>
              </li>
              <li class="nav-item" v-if="!isLogin">
                <RouterLink class="nav-link" :to="{name: 'login'}">Log In</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'community'}">Community</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'products'}">Products</RouterLink>
              </li>
              <li class="nav-item" v-if="isLogin">
                <RouterLink class="nav-link" :to="{name: 'profile'}">Profile</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'search'}">Find Nearby Banks</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'exchangeRateCalculator'}">Currency Converter</RouterLink>
              </li>
              <li class="nav-item" v-if="isLogin">
                <button class="nav-link btn" @click="LogOut">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <RouterView />
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/users'
import { computed } from 'vue'
const userStore = useUserStore()
const isLogin = computed(() => userStore.isLogin)
const LogOut = async () => {
  await userStore.LogOut()
}
</script>

<style scoped>
.navbar {
  background: linear-gradient(to right, #002b5c, #005c99);
  padding: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.nav-logo {
  width: 50px;
  height: auto;
  margin-right: 10px;
}

.navbar-brand {
  display: flex;
  align-items: center;
  font-size: 24px;
  font-weight: bold;
  color: white;
}

.nav-link {
  color: white !important;
  margin: 0 10px;
}

.nav-link:hover {
  color: #cccccc !important;
}

.nav-link.btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
}

.nav-link.btn:hover {
  color: #cccccc;
}
</style>
