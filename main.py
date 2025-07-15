from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

# CORS 설정 (모든 요청 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API 클라이언트 설정
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    try:
        # ✅ 시스템 프롬프트 설정
        system_prompt = {
            "role": "system",
            "content": (
                ""You are an expert in economic education. When requested, create example questions that elementary school students can easily understand, based on Bloom’s six levels of thinking (Knowledge, Comprehension, Application, Analysis, Evaluation, Creation). Provide 5 questions for each level:

At the Knowledge level, create questions that help students find accurate facts about economic exchanges with other countries.

At the Comprehension level, create questions that require students to explain the necessity of economic exchange with other countries.

At the Application level, create questions that help students apply what they have learned at the knowledge and comprehension levels to economic interactions with other countries or continents.

At the Analysis level, suggest questions that guide students to examine the benefits and problems that may arise from economic exchanges between Korea and other countries.

At the Evaluation level, suggest questions that involve setting criteria for economic exchanges between Korea and other countries or making decisions through comparisons. Please respond in Korean.
Make sure to include all levels in your response and provide enough detail so that none are left out." )
        }

        # GPT에 보낼 메시지 구성
        messages = [
            system_prompt,
            {"role": "user", "content": user_message}
        ]

        # GPT에 요청
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.7
        )

        answer = response.choices[0].message.content
        return {"response": answer}

    except Exception as e:
        return {"response": f"오류 발생: {str(e)}"}
