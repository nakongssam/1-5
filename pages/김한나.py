import streamlit as st
import random

st.set_page_config(
    page_title="약속 장소 정하기",
    page_icon="📍",
    layout="centered"
)

st.title("📍 약속 장소 정하기")
st.caption("만날 장소를 쉽고 빠르게 결정해보세요.")

# 세션 상태 초기화
if "places" not in st.session_state:
    st.session_state.places = []

if "votes" not in st.session_state:
    st.session_state.votes = {}

# 참석자
st.subheader("👥 참석자 정보")

participants = st.text_input(
    "참석자 이름 (쉼표로 구분)",
    placeholder="예: 민수, 지영, 수현"
)

# 지역 입력
st.subheader("🗺️ 만날 지역")

region = st.text_input(
    "지역 입력",
    placeholder="예: 천안, 강남, 종로"
)

st.divider()

# 장소 추가
st.subheader("➕ 장소 후보 추가")

with st.form("add_place_form"):
    place_name = st.text_input(
        "장소 이름",
        placeholder="예: 스타벅스 천안점"
    )

    category = st.selectbox(
        "카테고리",
        ["식당 🍜", "카페 ☕", "영화관 🎬", "쇼핑 🛍️", "기타 📍"]
    )

    submitted = st.form_submit_button("추가")

    if submitted:
        if place_name.strip():
            display_name = f"{place_name} ({category})"

            if display_name not in st.session_state.places:
                st.session_state.places.append(display_name)
                st.session_state.votes[display_name] = 0
                st.success("장소가 추가되었습니다.")
            else:
                st.warning("이미 등록된 장소입니다.")
        else:
            st.error("장소 이름을 입력해주세요.")

st.divider()

# 장소 목록
st.subheader("📋 장소 후보")

if st.session_state.places:

    for place in st.session_state.places:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(place)

        with col2:
            if st.button(
                "👍",
                key=f"vote_{place}"
            ):
                st.session_state.votes[place] += 1

    st.divider()

    # 투표 현황
    st.subheader("📊 투표 결과")

    for place in st.session_state.places:
        st.write(
            f"{place} : {st.session_state.votes[place]}표"
        )

    # 랜덤 추천
    if st.button("🎲 랜덤 장소 추천"):
        selected = random.choice(st.session_state.places)
        st.success(f"추천 장소: {selected}")

    # 최다 득표 장소
    if st.button("🏆 최종 장소 선정"):
        winner = max(
            st.session_state.votes,
            key=st.session_state.votes.get
        )

        st.balloons()
        st.success(
            f"최종 선정 장소는 '{winner}' 입니다!"
        )

else:
    st.info("장소 후보를 추가해주세요.")

st.divider()

# 초기화
if st.button("🗑️ 전체 초기화"):
    st.session_state.places = []
    st.session_state.votes = {}
    st.success("초기화 완료")
    st.rerun()
