import 'dotenv/config';
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import { OpenAI } from "openai";

const app = express();
const port = process.env.PORT || 3000;

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.use(cors());
app.use(bodyParser.json());

app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: message }],
      max_tokens: 150,
      temperature: 0.7,
    });

    res.json({
      reply: response.choices[0].message.content.trim(),
    });
  } catch (error) {
    console.error('Error generating response:', error);
    res.status(500).json({
      error: '서버 오류가 발생했습니다. 나중에 다시 시도해주세요.',
    });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
