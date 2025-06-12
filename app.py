import streamlit as st
import openai
import os

# 환경변수 또는 직접 입력
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Scoutly 자동 제안 메시지 생성기", layout="wide")

st.title("💼 Scoutly 자동 제안 메시지 생성기")

st.markdown("### 1️⃣ 채용 오더 입력")
jd_text = st.text_area("채용 오더를 여기에 입력해주세요", height=250)

st.markdown("### 2️⃣ 후보자 이력서 입력")
resume_text = st.text_area("후보자의 이력서 또는 요약 정보를 여기에 붙여넣어주세요", height=250)

if st.button("📨 제안 메시지 생성하기"):
    with st.spinner("GPT가 메시지를 생성 중입니다..."):
        prompt = f"""
        다음 정보를 바탕으로 헤드헌터가 후보자에게 보낼 2000자 이내의 정중하고 매력적인 포지션 제안 메시지를 작성해줘:

        [채용 포지션 정보]
        {jd_text}

        [후보자 정보]
        {resume_text}

        메시지 작성 가이드라인:
        1. 정중하고 전문적인 톤
        2. 후보자의 강점을 구체적으로 언급
        3. 포지션의 매력적인 부분 강조
        4. 간략한 회사 소개
        5. 다음 단계 안내
        6. 2000자 이내로 작성
        7. 한국어로 작성

        제목: [포지션명] 제안 드립니다.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.8
        )

        message = response.choices[0].message.content.strip()

    st.markdown("### ✉️ 생성된 제안 메시지")
    st.code(message, language="markdown")
    st.button("📋 복사하기", on_click=st.experimental_set_query_params, help="Ctrl+C로 복사해주세요")
