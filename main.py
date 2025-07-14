from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI        # ✅ 새 방식
import os

app = FastAPI()

# CORS – 모든 도메인 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 새 클라이언트 객체 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    try:
        completion = client.chat.completions.create(   # ✅ 새 메서드
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        answer = completion.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        return {"response": f"오류 발생: {e}"}
