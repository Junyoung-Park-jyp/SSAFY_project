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
              <li class="nav-item" v-if="isLogin">
                <button class="nav-link btn" @click="logOut">Logout</button>
              </li>
              <li class="nav-item" v-if="isLogin">
                <RouterLink class="nav-link" :to="{name: 'profile'}">Profile</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'community'}">Community</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'products'}">Products</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'search'}">Find Nearby Banks</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'exchangeRateCalculator'}">Currency Converter</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link" :to="{name: 'bankclerk'}">Bank Clerk</RouterLink>
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
const logOut = async () => {
  await userStore.LogOut()
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

.navbar {
  background: linear-gradient(135deg, #0f4c75, #3282b8, #bbe1fa);
  padding: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  font-family: 'Montserrat', sans-serif;
  border-bottom: 4px solid #3282b8;
}

.nav-logo {
  width: 60px;
  height: auto;
  margin-right: 15px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 2px solid #fff;
  border-radius: 50%;
}

.nav-logo:hover {
  transform: scale(1.2);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

.navbar-brand {
  display: flex;
  align-items: center;
  font-size: 28px;
  font-weight: bold;
  color: white;
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
}

.nav-link {
  color: white !important;
  margin: 0 15px;
  position: relative;
  padding: 5px 0;
  font-weight: 700;
  transition: color 0.3s ease, transform 0.3s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #ffffff;
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link:hover {
  color: #ffd700 !important;
  transform: scale(1.1);
}

.nav-link.btn {
  background: none;
  border: 2px solid white;
  color: white;
  cursor: pointer;
  padding: 5px 20px;
  transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;
  border-radius: 30px;
}

.nav-link.btn:hover {
  color: #0f4c75;
  background-color: #ffffff;
  box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
}

.nav-link.btn:active {
  background-color: rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
  .navbar-brand {
    font-size: 22px;
  }

  .nav-link {
    margin: 10px 0;
  }
}

.nav-item.active .nav-link {
  color: #ffd700 !important;
}

.navbar-nav.ml-auto {
  display: flex;
  align-items: center;
}

.navbar-collapse {
  justify-content: flex-end;
}

@keyframes navLinkGlow {
  0% {
    text-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
  }
  50% {
    text-shadow: 0 0 20px rgba(255, 215, 0, 1);
  }
  100% {
    text-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
  }
}

.navbar-brand:hover {
  animation: navLinkGlow 1s infinite;
}

.nav-link.active {
  color: #ffd700 !important;
}

.nav-link.active::after {
  width: 100%;
}
</style>



