import streamlit as st
import random

st.set_page_config(
    page_title="우리반 반장 도우미",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 우리반 반장 도우미")
st.caption("학생 주목 및 청소당번 자동 배정")

# 세션 상태 초기화
if "students" not in st.session_state:
    st.session_state.students = []

if "cleaning_result" not in st.session_state:
    st.session_state.cleaning_result = {}

# 학생 등록
st.header("👨‍🎓 학생 등록")

student_text = st.text_area(
    "학생 이름 입력 (한 줄에 한 명)",
    height=200,
    placeholder="""김민수
이영희
박준호"""
)

if st.button("학생 등록"):
    try:
        students = [
            s.strip()
            for s in student_text.split("\n")
            if s.strip()
        ]

        if students:
            st.session_state.students = students
            st.success(f"{len(students)}명 등록 완료")
        else:
            st.warning("학생 이름을 입력해주세요.")

    except Exception as e:
        st.error(f"오류 발생: {e}")

# 등록 현황
if st.session_state.students:

    st.info(
        f"현재 등록 학생 수 : {len(st.session_state.students)}명"
    )

    st.subheader("📋 학생 명단")
    st.write(", ".join(st.session_state.students))

st.divider()

# 학생 주목
st.header("👀 학생 주목시키기")

if st.session_state.students:

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎤 발표자 뽑기"):
            selected = random.choice(
                st.session_state.students
            )
            st.success(f"오늘의 발표자: {selected}")

    with col2:
        if st.button("❓ 질문 답변자 뽑기"):
            selected = random.choice(
                st.session_state.students
            )
            st.success(f"답변자: {selected}")

    if st.button("🎯 랜덤 학생 뽑기"):
        selected = random.choice(
            st.session_state.students
        )
        st.balloons()
        st.success(f"선택된 학생: {selected}")

else:
    st.info("학생을 먼저 등록하세요.")

st.divider()

# 청소당번
st.header("🧹 청소당번 정하기")

cleaning_places = [
    "교실 바닥",
    "복도",
    "창문",
    "분리수거",
    "칠판"
]

if st.session_state.students:

    if st.button("🧹 청소당번 자동 배정"):

        try:
            students_copy = st.session_state.students.copy()

            if len(students_copy) < len(cleaning_places):
                st.warning(
                    "학생 수가 청소구역보다 적습니다."
                )
            else:
                random.shuffle(students_copy)

                result = {}

                for i, area in enumerate(cleaning_places):
                    result[area] = students_copy[i]

                st.session_state.cleaning_result = result

        except Exception as e:
            st.error(f"오류 발생: {e}")

# 결과 표시
if st.session_state.cleaning_result:

    st.subheader("📋 청소당번 결과")

    for area, student in st.session_state.cleaning_result.items():
        st.write(f"✅ {area} : {student}")

st.divider()

# 초기화
st.header("🔄 초기화")

col1, col2 = st.columns(2)

with col1:
    if st.button("학생 명단 초기화"):
        st.session_state.students = []
        st.session_state.cleaning_result = {}
        st.success("학생 명단 삭제 완료")
        st.rerun()

with col2:
    if st.button("청소당번 초기화"):
        st.session_state.cleaning_result = {}
        st.success("청소당번 삭제 완료")
        st.rerun()
