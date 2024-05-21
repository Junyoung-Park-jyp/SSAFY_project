<template>
  <div class="container mt-5 product-view">
    <nav class="nav nav-pills justify-content-center mb-4">
      <RouterLink class="nav-link" :to="{name: 'deposit'}">정기예금</RouterLink>
      <RouterLink class="nav-link" :to="{name: 'saving'}">정기적금</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<style scoped>
.product-view {
  background: linear-gradient(to right, #ffffff, #f7f7f7);
  padding: 60px;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  margin-top: 40px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: all 0.3s ease;
}

.product-view:hover {
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

h1 {
  color: #004080;
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 30px;
}

.nav-pills {
  border-bottom: 2px solid #ddd;
  padding-bottom: 10px;
}

.nav-pills .nav-link {
  margin: 0 15px;
  padding: 12px 25px;
  background-color: #004080;
  color: white;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 500;
  transition: background-color 0.3s, transform 0.3s;
}

.nav-pills .nav-link:hover {
  background-color: #0059b3;
  transform: translateY(-2px);
}

.nav-pills .nav-link.active {
  background-color: #003366;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
