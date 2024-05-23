<template>
  <div class="chatbot">
    <div class="messages">
      <div v-for="message in messages" :key="message.id" class="message">
        <div :class="{'user-message': message.sender === 'user', 'bot-message': message.sender === 'bot'}">
          <p>{{ message.text }}</p>
        </div>
      </div>
    </div>
    <input v-model="userInput" @keyup.enter="sendMessage" placeholder="질문을 입력하세요..."/>
    <button @click="sendMessage">보내기</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInput: '',
      messages: [],
      user: {
        age: 30,
        current_balance: 1000000,
        annual_salary: 50000000,
        saving_preference: 'conservative',
        favorite_bank: 'KB'
      }
    };
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === '') return;
      
      this.messages.push({ id: Date.now(), text: this.userInput, sender: 'user' });
      try {
        const response = await axios.post('http://127.0.0.1:8000/chatbot/', {
          message: this.userInput,
          user: this.user
        });
        this.messages.push({ id: Date.now(), text: response.data.reply, sender: 'bot' });
      } catch (error) {
        console.error(error);
        this.messages.push({ id: Date.now(), text: '서버 오류가 발생했습니다. 나중에 다시 시도해주세요.', sender: 'bot' });
      }
      this.userInput = '';
    }
  }
};
</script>

<style scoped>
.chatbot {
  width: 300px;
  margin: 0 auto;
}
.messages {
  max-height: 400px;
  overflow-y: auto;
  margin-bottom: 10px;
}
.message {
  margin: 10px 0;
}
.user-message {
  text-align: right;
}
.bot-message {
  text-align: left;
}
</style>
