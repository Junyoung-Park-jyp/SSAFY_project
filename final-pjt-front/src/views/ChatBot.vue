<template>
  <div class="chat-container">
    <div class="chat-box">
      <div class="chat-log" ref="chatLog">
        <div v-for="message in messages" :key="message.id" :class="['message', message.sender]">
          <div class="message-content">
            <p>{{ message.text }}</p>
          </div>
        </div>
      </div>
      <form @submit.prevent="sendMessage" class="input-box">
        <input type="text" v-model="userInput" placeholder="질문을 입력하세요..." class="form-control" />
        <button type="submit" class="btn btn-primary">전송</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useProductStore } from '@/stores/products'
import { useUserStore } from '@/stores/users'
import axios from 'axios'

const userInput = ref('')
const messages = ref([
  { id: 1, sender: 'bot', text: '안녕하세요! 무엇을 도와드릴까요?' }
])
const productStore = useProductStore()
const userStore = useUserStore()
const chatLog = ref(null)

const sendMessage = async () => {
  const userMessage = userInput.value.trim()
  if (userMessage) {
    messages.value.push({ id: Date.now(), sender: 'user', text: userMessage })
    userInput.value = ''
    await nextTick()
    chatLog.value.scrollTop = chatLog.value.scrollHeight

    const response = await getChatBotResponse(userMessage)
    messages.value.push({ id: Date.now(), sender: 'bot', text: response })
    await nextTick()
    chatLog.value.scrollTop = chatLog.value.scrollHeight
  }
}

const getChatBotResponse = async (message) => {
  try {
    const user = userStore.user
    const response = await axios.post('http://127.0.0.1:8000/api/v1/chatbot/', {
      message,
      user: {
        age: user.age,
        bank: user.bank
      }
    })
    return response.data.reply
  } catch (error) {
    console.error(error)
    return '죄송합니다, 현재 답변을 드릴 수 없습니다.'
  }
}

onMounted(() => {
  chatLog.value.scrollTop = chatLog.value.scrollHeight
})
</script>

<style scoped>
.chat-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f7f7f7;
}

.chat-box {
  width: 400px;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
}

.chat-log {
  height: 300px;
  overflow-y: auto;
  padding: 20px;
  background-color: #e9e9e9;
}

.message {
  margin-bottom: 10px;
}

.message.user .message-content {
  background-color: #007bff;
  color: white;
  border-radius: 10px;
  padding: 10px;
  max-width: 75%;
  margin-left: auto;
}

.message.bot .message-content {
  background-color: #f1f1f1;
  border-radius: 10px;
  padding: 10px;
  max-width: 75%;
}

.input-box {
  display: flex;
  padding: 10px;
  background-color: #e9e9e9;
}

.form-control {
  flex-grow: 1;
  border: none;
  border-radius: 5px;
  padding: 10px;
}

.btn-primary {
  margin-left: 10px;
  padding: 10px 20px;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>
