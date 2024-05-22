<template>
  <div class="home">
    <header class="hero">
      <div class="slideshow-container">
        <div class="slideshow">
          <div class="slide">
            <img src="@/assets/slide1.png" alt="Slide 1">
          </div>
          <div class="slide">
            <img src="@/assets/slide2.png" alt="Slide 2">
          </div>
          <div class="slide">
            <img src="@/assets/slide3.png" alt="Slide 3">
          </div>
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
    <div class="chatbot">
      <button class="chatbot-toggle" @click="toggleChatbot">
        <img src="@/assets/slide7.png" alt="Chatbot Icon">
      </button>
      <div v-if="showChatbot" class="chatbot-window">
        <div class="chatbot-header">
          <h3>대화</h3>
          <button class="close-btn" @click="toggleChatbot">×</button>
        </div>
        <div class="chatbot-messages">
          <div v-for="(msg, index) in messages" :key="index" :class="{'user-msg': msg.user, 'bot-msg': !msg.user}">
            <p>{{ msg.text }}</p>
          </div>
        </div>
        <form @submit.prevent="sendMessage">
          <input type="text" v-model="userMessage" placeholder="질문을 입력하세요..." required>
          <button type="submit">보내기</button>
        </form>
      </div>
    </div>
    <footer class="footer">
      <p>&copy; 2024 Bank For You. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeView',
  data() {
    return {
      showChatbot: false,
      userMessage: '',
      messages: [
        { text: '병신아 무엇을 도와드릴까요?', user: false }
      ]
    };
  },
  methods: {
    toggleChatbot() {
      this.showChatbot = !this.showChatbot;
    },
    async sendMessage() {
      const userMsg = this.userMessage;
      this.messages.push({ text: userMsg, user: true });
      this.userMessage = '';

      try {
        const response = await axios.post('http://localhost:3000/api/chat', { message: userMsg });
        this.messages.push({ text: response.data.reply, user: false });
      } catch (error) {
        console.error('Error sending message:', error);
        this.messages.push({ text: '서버 오류가 발생했습니다. 나중에 다시 시도해주세요.', user: false });
      }
    }
  }
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

.chatbot {
  position: fixed;
  bottom: 80px;
  right: 20px;
  z-index: 1000;
}

.chatbot-toggle {
  background: #005c99;
  color: white;
  border: none;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.chatbot-toggle img {
  width: 100%;
  height: auto;
  display: block;
}

.chatbot-window {
  position: fixed;
  bottom: 120px;
  right: 20px;
  width: 300px;
  max-height: 500px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
}

.chatbot-header {
  background: #005c99;
  color: white;
  padding: 10px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chatbot-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
}

.user-msg {
  text-align: right;
}

.bot-msg {
  text-align: left;
}

form {
  display: flex;
  border-top: 1px solid #ccc;
}

input {
  flex: 1;
  padding: 10px;
  border: none;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}

button {
  background: #005c99;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-bottom-right-radius: 15px;
}
</style>
