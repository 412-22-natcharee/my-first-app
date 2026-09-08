import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:  
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:  
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:  
    st.session_state.ans10_val = ""

# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 8
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 9
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 10
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
  st.balloons()
  score = 0

  u_ans1 = ans1.strip().lower()
  u_ans2 = ans2.strip().lower()
  u_ans3 = ans3.strip().lower()
  u_ans4 = ans4.strip().lower()
  u_ans5 = ans5.strip().lower()
  u_ans6 = ans6.strip().lower()
  u_ans7 = ans7.strip().lower()
  u_ans8 = ans8.strip().lower()
  u_ans9 = ans9.strip().lower()
  u_ans10 = ans10.strip().lower()

# ตรวจข้อ 1
if u_ans1 == "thailand":
    st.success("✅ ข้อ 1: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

# ตรวจข้อ 2
if u_ans2 == "united states":
    st.success("✅ ข้อ 2: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

# ตรวจข้อ 3
if u_ans3 == "china":
    st.success("✅ ข้อ 3: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

# ตรวจข้อ 4
if u_ans4 == "united kingdom":
    st.success("✅ ข้อ 4: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

# ตรวจข้อ 5
if u_ans5 == "australia":
    st.success("✅ ข้อ 5: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

# ตรวจข้อ 6
if u_ans6 == "france":
    st.success("✅ ข้อ 6: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

# ตรวจข้อ 7
if u_ans7 == "japan":
    st.success("✅ ข้อ 7: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")

# ตรวจข้อ 8
if u_ans8 == "south korea":
    st.success("✅ ข้อ 8: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")

# ตรวจข้อ 9
if u_ans9 == "india":
    st.success("✅ ข้อ 9: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")

# ตรวจข้อ 10
if u_ans10 == "canada":
    st.success("✅ ข้อ 10: ถูกต้อง")
    score += 1
else:
    st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")

  st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

if score == 10:
  st.success("🥳 You pass!")
if score == 5-9:
  st.success("🥰Well done")
else:
  st.error("😭You fail")

# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
  time_left = int(300 - (time.time() - st.session_state.start))

  if time_left > 0:
    st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
  else:
      st.session_state.is_ended = True
      st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
  "ข้อ 1: Southeast Asia,never colonized `t _ a _ l _ _ d` . 🇹🇭",
  value=st.session_state.ans1_val,
)
ans2 = st.text_input(
  "ข้อ 2: North America,Statue of Liberty `u _ i t _ d s _ a _ e s`. 🇺🇸",
  value=st.session_state.ans2_val,
)
ans3 = st.text_input(
  "ข้อ 3: Largest population,Great Wall `c _ i _ a` . 🇨🇳",
  value=st.session_state.ans3_val,
)
ans4 = st.text_input(
  "ข้อ 4: London,Big Ben `u n _ t _ d k _ n _ d _ m` . 🇬🇧",
  value=st.session_state.ans4_val,
)
ans5 = st.text_input(
  "ข้อ 5: Kangaroos,Great Barrier Reef `a _ s t _  a _ i a` . 🇦🇺",
  value=st.session_state.ans5_val,
)
ans6 = st.text_input(
  "ข้อ 6: Eiffel Tower , wine , pastries `f _ a n c _` . 🇫🇷",
  value=st.session_state.ans6_val,
)
ans7 = st.text_input(
  "ข้อ 7: Island country , Mount Fuji , sushi `j _ p _ n` . 🇯🇵",
  value=st.session_state.ans7_val,
)
ans8 = st.text_input(
  "ข้อ 8: K-pop, kimchi, Seoul `s _ u t _ k _ r e _` . 🇰🇷",
  value=st.session_state.ans8_val,
)
ans9 = st.text_input(
  "ข้อ 9: Largest country, Moscow `i _ d _ a` . 🇨🇮",
  value=st.session_state.ans9_val,
)
ans10 = st.text_input(
  "ข้อ 10: Maple leaf,second largest country `c _ n a _ _` . 🇨🇦",
  value=st.session_state.ans10_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8
st.session_state.ans9_val = ans9
st.session_state.ans10_val = ans10

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
   if st.button("📥 ส่งคำตอบ"):
       st.session_state.is_ended = True
       st.rerun()

   time.sleep(1)
   st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)


st.divider()
st.write("นางสาวณัฐชารี คงสุนทร เลขที่ 22 ม.4/12")
