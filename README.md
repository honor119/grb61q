# GPT Chat API (FastAPI) for Render

이 프로젝트는 **FastAPI**로 만든 간단한 ChatGPT 프록시 API입니다.  
Render의 무료 웹 서비스 플랜에서 바로 배포할 수 있습니다.

## 🗂️ 구조
```
main.py          # FastAPI 애플리케이션
requirements.txt # 의존성 목록
render.yaml      # Render 배포 설정
.gitignore
```
## 🔧 로컬 실행 (옵션)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
uvicorn main:app --reload
```

## 🚀 Render 배포 방법
1. GitHub에 새로운 레포지터리를 만들고 이 파일들을 업로드(push) 합니다.
2. Render(https://render.com)에 로그인 ➜ `New +` ➜ **Web Service** 선택
3. GitHub 레포 선택 후, 설정은 `render.yaml` 덕분에 자동으로 채워집니다.
4. **Environment Variables** 탭에서 `OPENAI_API_KEY`를 추가하고 GPT 키 값을 입력합니다.
5. 배포가 완료되면 `https://<서비스이름>.onrender.com/chat` 엔드포인트가 생성됩니다.

## 📄 엔드포인트 예시
- POST `/chat`
```json
{ "message": "호랑이는 어디 살아요?" }
```

### 응답
```json
{ "response": "GPT의 답변..." }
```

---