import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)


import streamlit as st
import time
import pandas as pd
from backend.chatbot import ask_gemini
from backend.db import get_notices, get_attendance, get_usage, get_chat_history
from supabase import create_client

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Smart Campus Assistant", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.card {
    background-color:#1E293B;
    padding:20px;
    color:#F1F5F9;
    border-radius:12px;
    margin:10px 0;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("🎓 Smart Campus")
menu = st.sidebar.radio(
    "Go to",
    ["Home", "Ask Assistant", "Dashboard", "Notices", "Profile", "Login"]
)

# ================= HOME =================
if menu == "Home":
    st.markdown("## 🎓 Smart Campus Assistant")
    st.write("AI-powered assistant for smart campus services.")

    col1, col2, col3 = st.columns(3)
    col1.metric("👨‍🎓 Students", "5000+")
    col2.metric("📚 Services", "10+")
    col3.metric("⚡ Response Time", "<1 sec")

# ================= ASK ASSISTANT =================
elif menu == "Ask Assistant":
    st.header("🤖 Ask Gemini")

    question = st.text_input(
        "Type your question here",
        key="gemini_input"
    )

    if st.button("Ask AI"):
        if question:
            with st.spinner("Gemini is thinking..."):
                answer = ask_gemini(question)
            st.success(answer)

# ================= DASHBOARD =================
elif menu == "Dashboard":
    st.header("📊 Smart Campus Dashboard")

    # Notices
    st.subheader("📢 Notices")
    for n in get_notices():
        st.markdown(f"**{n['title']}** — {n['body']}  \n📅 *{n['date']}*")

    # Attendance
    st.subheader("📊 Attendance (CSE-2)")
    df_att = pd.DataFrame(get_attendance("CSE-2"))
    if not df_att.empty:
        st.line_chart(df_att.set_index("date")["percent"])

    # Usage
    st.subheader("🌱 Sustainability Usage")
    df_usage = pd.DataFrame(get_usage())
    if not df_usage.empty:
        st.line_chart(df_usage.set_index("date")[["electricity_kwh", "water_liters"]])

    # Chat history
    st.subheader("🕘 Chat History")
    for chat in get_chat_history():
        st.write(f"**Student:** {chat['question']}")
        st.write(f"➡️ {chat['answer']}")

# ================= NOTICES =================
elif menu == "Notices":
    st.markdown("""
    <div class="card">
        <h4>📢 Holiday Notice</h4>
        <p>Campus closed on 25th December</p>
    </div>
    """, unsafe_allow_html=True)

# ================= PROFILE =================
elif menu == "Profile":
    st.header("👤 Student Profile")
    st.write("Name: Divya")
    st.write("Course: B.Tech AI/ML")

# ================= LOGIN =================# 
elif menu == "Login":
    from supabase import create_client

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    st.header("🔐 Login / Register")

    email = st.text_input("Email", key="auth_email")
    password = st.text_input("Password", type="password", key="auth_password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Register"):
            try:
                supabase.auth.sign_up({
                    "email": email,
                    "password": password
                })
                st.success("Registered successfully! Now login.")
            except Exception as e:
                st.error(str(e))

    with col2:
        if st.button("Login"):
            try:
                supabase.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })
                st.success("Login successful!")
                st.session_state.logged_in = True
            except Exception as e:
                st.error(str(e))


# ================= FOOTER =================
st.markdown("---")
st.caption("🚀 Built by Divya | Powered by Gemini & Supabase")

