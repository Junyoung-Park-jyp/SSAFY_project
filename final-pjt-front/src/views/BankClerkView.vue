<template>
    <div>
        <div class="slideshow-container">
        <div class="slideshow">

          <div class="slide">
            <img src="@/assets/slide4.png" alt="Slide 4">
          </div>
          <div class="slide">
            <img src="@/assets/slide5.png" alt="Slide 5">
          </div>
          <div class="slide">
            <img src="@/assets/slide6.png" alt="Slide 6">
          </div>
          <div class="slide">
            <img src="@/assets/slide7.png" alt="Slide 7">
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
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
</style>