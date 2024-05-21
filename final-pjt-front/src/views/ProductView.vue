<template>
  <div class="container mt-4 products">
    <h1 style="text-align: center;">Products</h1>
    <nav class="product-nav">
      <RouterLink :to="{ name: 'deposit' }" class="nav-link">정기예금</RouterLink>
      <RouterLink :to="{ name: 'saving' }" class="nav-link">정기적금</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script>
export default {
  name: 'ProductView',
};
</script>

<style scoped>
.products {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h1 {
  color: #002b5c;
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.product-nav {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.nav-link {
  padding: 10px 20px;
  background-color: #005c99;
  color: white;
  border-radius: 5px;
  text-decoration: none;
}

.nav-link:hover {
  background-color: #002b5c;
}
</style>
