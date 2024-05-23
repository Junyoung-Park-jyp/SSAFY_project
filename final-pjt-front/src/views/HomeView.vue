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
          <h3>Chat with Bot</h3>
          <button class="close-btn" @click="toggleChatbot">×</button>
        </div>
        <div class="chatbot-messages">
          <div v-for="(msg, index) in messages" :key="index" :class="{'user-msg': msg.user, 'bot-msg': !msg.user}">
            <p v-if="msg.user">{{ msg.text }}</p>
            <p v-else v-html="msg.text"></p>
          </div>
        </div>
        <form @submit.prevent="sendMessage">
          <input type="text" v-model="userMessage" placeholder="Enter your question..." required>
          <button type="submit">Send</button>
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
import { useUserStore } from '@/stores/users';

export default {
  name: 'HomeView',
  data() {
    return {
      showChatbot: false,
      userMessage: '',
      messages: []
    };
  },
  methods: {
    toggleChatbot() {
      this.showChatbot = !this.showChatbot;
    },
    async sendMessage() {
  const userStore = useUserStore();
  // 로그인 상태 확인
  if (!userStore.isLogin) {
    // 로그인되지 않은 경우, 메시지 전송하지 않고 종료
    this.messages.push({ text: '챗봇 서비스를 이용하시려면 로그인해주세요.', user: false });
    return;
  }

  const userlist = await userStore.getProfile(); // 사용자 프로필을 비동기로 가져옴
  const userMsg = this.userMessage;
  this.messages.push({ text: userMsg, user: true });
  this.userMessage = '';
  const user = userlist.user_info;
  try {
    const response = await axios.post('http://127.0.0.1:8000/chatbot/', {
      message: userMsg,
      user: {
        age: user.age,
        current_balance: user.current_balance,
        annual_salary: user.annual_salary,
        bank: user.bank
      }
    });
    const botReply = response.data.reply.replace(/\n/g, '<br>');
    this.messages.push({ text: botReply, user: false });
  } catch (error) {
    console.error('Error sending message:', error);
    this.messages.push({ text: 'Server error occurred. Please try again later.', user: false });
  }
}

  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {
  font-family: 'Montserrat', sans-serif;
  background: #f4f4f9;
  color: #333;
  margin: 0;
  padding: 0;
}

.home {
  text-align: center;
  font-family: 'Montserrat', sans-serif;
}

.hero {
  position: relative;
  width: 100%;
  height: 400px;
  overflow: hidden;
  background: linear-gradient(to right, #0f4c75, #3282b8);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
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
  padding: 60px 20px;
  flex-wrap: wrap;
  background: #e0f7fa;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  margin-top: -30px;
  position: relative;
  z-index: 1;
}

.feature {
  background: white;
  padding: 30px;
  margin: 10px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1 1 calc(30% - 20px);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.feature h2 {
  margin-top: 0;
  font-size: 28px;
  color: #0f4c75;
}

.feature p {
  font-size: 18px;
  color: #555;
}

.footer {
  background: #0f4c75;
  color: white;
  padding: 20px;
  text-align: center;
  position: relative;
  width: 100%;
  bottom: 0;
  box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);
  margin-top: 40px;
}

.chatbot {
  position: fixed;
  bottom: 80px;
  right: 20px;
  z-index: 1000;
}

.chatbot-toggle {
  background: linear-gradient(to right, #3282b8, #bbe1fa);
  color: white;
  border: none;
  border-radius: 50%;
  padding: 15px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.chatbot-toggle img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 50%;
}

.chatbot-toggle:hover {
  transform: scale(1.1);
  background-color: #3282b8;
}

.chatbot-window {
  position: fixed;
  bottom: 120px;
  right: 20px;
  width: 350px;
  max-height: 500px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chatbot-header {
  background: #3282b8;
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
  background: #f4f4f9;
}

.user-msg {
  text-align: right;
  margin-bottom: 10px;
}

.bot-msg {
  text-align: left;
  margin-bottom: 10px;
}

.user-msg p, .bot-msg p {
  background: #e0f7fa;
  padding: 10px;
  border-radius: 15px;
  display: inline-block;
  max-width: 80%;
}

form {
  display: flex;
  border-top: 1px solid #ccc;
  background: white;
  padding: 10px;
}

input {
  flex: 1;
  padding: 10px;
  border: none;
  border-radius: 20px;
  margin-right: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

button {
  background: #3282b8;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 20px;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

button:hover {
  background-color: #0f4c75;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>

