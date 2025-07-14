from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# CORS 설정 (모든 도메인 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 환경변수에서 API 키 읽기
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        answer = response.choices[0].message["content"]
        return {"response": answer}
    except Exception as e:
        # 오류 메시지를 클라이언트에 반환
        return {"response": f"오류 발생: {str(e)}"}