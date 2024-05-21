<template>
    <div>
      <button @click="toggleChatbot" class="chatbot-button">
        <img src="@/assets/chatbot-icon.png" alt="Chatbot Icon">
      </button>
      <div v-if="showChatbot" class="chatbot-window" ref="chatWindow">
        <div class="chatbot-header">
          <h2>대화</h2>
          <button @click="toggleChatbot" class="close-button">×</button>
        </div>
        <div class="chatbot-body">
          <div class="message" v-for="(message, index) in messages" :key="index">
            <div class="message-content" :class="message.type">
              <p>{{ message.content }}</p>
            </div>
          </div>
        </div>
        <div class="chatbot-footer">
          <input type="text" v-model="userMessage" placeholder="질문을 입력하세요..." @keyup.enter="sendMessage">
          <button @click="sendMessage">보내기</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        showChatbot: false,
        userMessage: '',
        messages: [
          { type: 'bot', content: '안녕하세요! 무엇을 도와드릴까요?' }
        ]
      };
    },
    methods: {
      toggleChatbot() {
        this.showChatbot = !this.showChatbot;
      },
      async sendMessage() {
        if (this.userMessage.trim() === '') return;
        this.messages.push({ type: 'user', content: this.userMessage });
        const message = this.userMessage;
        this.userMessage = '';
        try {
          const response = await axios.post('http://localhost:3000/api/chat', { message });
          this.messages.push({ type: 'bot', content: response.data.reply });
        } catch (error) {
          this.messages.push({ type: 'bot', content: '서버 오류가 발생했습니다. 나중에 다시 시도해주세요.' });
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .chatbot-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #005c99;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    cursor: pointer;
  }
  
  .chatbot-button img {
    width: 100%;
    height: auto;
  }
  
  .chatbot-window {
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 400px;
    max-height: 600px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    resize: both;
    min-width: 300px;
    min-height: 200px;
  }
  
  .chatbot-header {
    background: #005c99;
    color: white;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .close-button {
    background: none;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
  }
  
  .chatbot-body {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .message-content {
    padding: 10px;
    border-radius: 10px;
    max-width: 80%;
    word-wrap: break-word;
  }
  
  .message-content.bot {
    background: #f1f1f1;
    align-self: flex-start;
  }
  
  .message-content.user {
    background: #005c99;
    color: white;
    align-self: flex-end;
  }
  
  .chatbot-footer {
    display: flex;
    padding: 10px;
    border-top: 1px solid #ddd;
  }
  
  .chatbot-footer input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 10px;
  }
  
  .chatbot-footer button {
    padding: 10px 20px;
    background-color: #005c99;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  