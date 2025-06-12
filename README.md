# Scoutly 자동 제안 메시지 생성기

이 앱은 헤드헌터를 위한 **GPT 기반 자동 제안 메시지 생성 도구**입니다.
Streamlit을 기반으로 빠르게 UI를 구성했으며, 채용 오더와 후보자 이력서를 입력하면 AI가 2000자 이내의 맞춤형 메시지를 생성해줍니다.

---

## 🚀 주요 기능

- 채용 오더(JD) 입력
- 후보자 이력서 또는 요약 정보 입력
- GPT-4 기반 자동 제안 메시지 생성 (한국어, 2000자 이내)
- 생성된 메시지 복사 기능 제공

---

## 🛠️ 설치 방법

1. Python 3.8+ 설치
2. 의존성 설치:
```bash
pip install -r requirements.txt
```

3. OpenAI API 키 설정:
- `.streamlit/secrets.toml` 파일 생성 후 다음과 같이 입력:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

4. 실행:
```bash
streamlit run app.py
```

---

## 💡 예시 화면

<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="100"/>

> 채용 오더와 이력서를 입력하고 버튼을 누르면 GPT가 제안 메시지를 생성합니다.

---

## 📄 라이선스
MIT License
