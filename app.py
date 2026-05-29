import streamlit as st

st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💕"
)

st.title("💕 연애 코칭 앱")

st.write("연애 고민을 입력하면 간단한 조언을 해드립니다!")

user_input = st.text_input("고민을 입력하세요")

if st.button("조언 받기"):
    if user_input == "":
        st.warning("고민을 입력해주세요!")
    else:
        # 아주 간단한 규칙 기반 답변
        if "고백" in user_input:
            answer = "진심을 담아 솔직하게 이야기해보세요 😊"
        elif "싸움" in user_input:
            answer = "감정보다 대화를 우선해보는 것이 좋아요 💬"
        elif "이별" in user_input:
            answer = "충분히 힘들 수 있어요. 스스로를 먼저 돌봐주세요 🌱"
        else:
            answer = "상대방의 마음을 존중하며 천천히 대화해보세요 💕"

        st.success(answer)
