<template>
  <div>
    <h1>Products</h1>
    <nav>
      <RouterLink :to="{name: 'deposit'}">정기예금</RouterLink> | 
      <RouterLink :to="{name: 'saving'}">정기적금</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>
