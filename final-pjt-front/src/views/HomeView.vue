<template>
  <div class="home">
      <header class="hero">
        <div class="slideshow-container">
          <div class="slideshow">
            <div class="slide">
              <img src="@/assets/slide10.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide10.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
            <div class="slide">
              <img src="@/assets/slide8.gif" alt="Slide 3">
            </div>
          </div>
        </div>
      </div>
    </header>
    <section class="features">
      <div class="feature">
        <h2>Easy Banking</h2>
        <p>Manage your finances with ease and convenience.</p>
      </div>
      <div class="feature">
        <h2>Secure Transactions</h2>
        <p>Experience top-notch security for all your transactions.</p>
      </div>
      <div class="feature">
        <h2>24/7 Support</h2>
        <p>We are here to help you anytime, anywhere.</p>
      </div>
    </section>
    <footer class="footer">
      <p>&copy; 2024 Bank For You. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.home {
  text-align: center;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.hero {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  background: #f0f0f0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.slideshow-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slideshow {
  display: flex;
  width: 100%;
  animation: slide 12s infinite;
}

.slide {
  width: 33.333%;
  flex-shrink: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slide img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

@keyframes slide {
  0%, 20%, 100% {
    transform: translateX(0%);
  }
  20.01%, 40% {
    transform: translateX(-33.333%);
  }
  40.01%, 60% {
    transform: translateX(-66.666%);
  }
  60.01%, 80% {
    transform: translateX(-100%);
  }
  80.01%, 100% {
    transform: translateX(-133.333%);
  }
}

.features {
  display: flex;
  justify-content: space-around;
  padding: 40px 20px;
  flex-wrap: wrap;
}

.feature {
  background: white;
  padding: 30px;
  margin: 10px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(33.333% - 40px);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.feature h2 {
  margin-top: 0;
  font-size: 28px;
}

.feature p {
  font-size: 18px;
}

.footer {
  background: #002b5c;
  color: white;
  padding: 20px;
  text-align: center;
  position: fixed;
  width: 100%;
  bottom: 0;
  box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);
}
</style>
