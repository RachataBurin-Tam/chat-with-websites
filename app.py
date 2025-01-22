import streamlit as st
from datetime import datetime

# ตั้งค่าหน้าเพจ
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖"
)

# ฟังก์ชันสำหรับประมวลผลข้อความและส่งคำตอบกลับ
def get_bot_response(user_input):
    # ตัวอย่างการตอบกลับแบบง่าย
    responses = {
        "สวัสดี": "สวัสดีครับ! มีอะไรให้ช่วยไหมครับ?",
        "ชื่ออะไร": "ผมชื่อ ChatBot ครับ ยินดีที่ได้รู้จัก",
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
st.title("🤖 Simple Chatbot")
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