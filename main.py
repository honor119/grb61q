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
                "너는 교육 전문가야. 사용자가 요청하면 Bloom의 6가지 사고 수준(지식, 이해, 적용, 분석, 평가, 창안)에 따라 각 수준별로 초등학생이 이해할 수 있는 쉬운 질문을 5개씩 만들어줘."
            )
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
            max_tokens=1000,
            temperature=0.7
        )

        answer = response.choices[0].message.content
        return {"response": answer}

    except Exception as e:
        return {"response": f"오류 발생: {str(e)}"}
