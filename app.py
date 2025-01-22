import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os

# โหลดค่าจาก .env file
load_dotenv()

# อ่านค่าจาก environment variables
BOT_NAME = os.getenv('BOT_NAME', 'ChatBot')
WELCOME_TEXT = os.getenv('WELCOME_TEXT', 'สวัสดีครับ มีอะไรให้ช่วยไหมครับ?')

# ตั้งค่าหน้าเพจ
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖"
)

# แสดงค่าที่อ่านได้จาก .env ใน sidebar
with st.sidebar:
    st.write("### Environment Variables")
    st.write(f"BOT_NAME: {BOT_NAME}")
    st.write(f"WELCOME_TEXT: {WELCOME_TEXT}")

# ฟังก์ชันสำหรับประมวลผลข้อความและส่งคำตอบกลับ
def get_bot_response(user_input):
    responses = {
        "สวัสดี": WELCOME_TEXT,
        "ชื่ออะไร": f"ผมชื่อ {BOT_NAME} ครับ ยินดีที่ได้รู้จัก",
        "ขอบคุณ": "ด้วยความยินดีครับ",
        "ลาก่อน": "แล้วเจอกันใหม่นะครับ!"
    }
    
    # ตรวจสอบคำสำคัญในข้อความ
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    
    return "ขอโทษครับ ผมไม่เข้าใจคำถาม กรุณาถามใหม่อีกครั้ง"

# สร้าง session state สำหรับเก็บประวัติการสนทนา
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# ส่วนหัวของแอพ
st.title(f"🤖 {BOT_NAME}")
st.write("คุยกับผมได้เลยครับ!")

# ส่วนรับข้อความจากผู้ใช้
user_input = st.chat_input("พิมพ์ข้อความของคุณที่นี่:")

# จัดการกับข้อความที่ได้รับ
if user_input:
    # เพิ่มข้อความผู้ใช้ลงในประวัติ
    st.session_state.chat_history.append({
        'role': 'user',
        'message': user_input
    })
    
    # รับคำตอบจาก bot และเพิ่มลงในประวัติ
    bot_response = get_bot_response(user_input)
    st.session_state.chat_history.append({
        'role': 'bot',
        'message': bot_response
    })

# ส่วนแสดงประวัติการสนทนา
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            with st.chat_message("user"):
                st.write(message['message'])
        else:
            with st.chat_message("assistant"):
                st.write(message['message'])

# เพิ่มปุ่มล้างประวัติการสนทนา
if st.button("ล้างประวัติการสนทนา"):
    st.session_state.chat_history = []
    st.rerun()

# แสดงคำแนะนำการใช้งาน
with st.expander("วิธีใช้งาน"):
    st.write("""
    1. พิมพ์ข้อความที่ต้องการในช่องข้อความด้านล่าง
    2. กด Enter เพื่อส่งข้อความ
    3. Bot จะตอบกลับอัตโนมัติ
    4. สามารถกดปุ่ม 'ล้างประวัติการสนทนา' เพื่อเริ่มต้นใหม่
    
    ตัวอย่างคำถามที่ Bot เข้าใจ:
    - สวัสดี
    - ชื่ออะไร
    - ขอบคุณ
    - ลาก่อน
    """)