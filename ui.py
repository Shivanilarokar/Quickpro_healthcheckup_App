import streamlit as st
import time

# Page config
st.set_page_config(page_title="🩺 HealthCheck App", layout="centered")
st.title("🩺 QuickHealth Pro Max – Interactive Symptom Checker") 

# Greeting based on session
st.markdown("👋 Hello there! Let's check how you're doing today.") 

# === Section 1: User Info ===
st.markdown("## 👤 Personal Information")
name = st.text_input("👤 Name:")
age = st.text_input("🎂 Age:")
gender = st.selectbox("🚻 Gender:", ["Select", "male", "female", "other"])
city = st.text_input("🏙️ City:")

# === Section 2: Health Symptoms ===
st.markdown("---")
st.markdown("## 🤒 Health Symptoms")
main_symptoms = st.selectbox("🩺 Main Symptom:", ["Select", "fever", "cough", "fatigue", "headache", "chest pain", "breathlessness"])
fever = st.text_input("🌡️ Body Temperature (°F):")
no_of_sick_days = st.slider("📆 Days You've Been Sick:", 0, 30, 0)
smoking_habit = st.radio("🚬 Do you smoke?", ["yes", "no"])
sleep_hours = st.slider("🛏️ Hours of Sleep per Night:", 0, 12, 7)
mood = st.selectbox("🧠 Mood:", ["Select", "calm", "anxious", "sad", "irritable"])
pre_existing_conditions = st.radio("🏥 Pre-existing Conditions:", ["yes", "no"])
cough_days = st.text_input("🤧 Days Since Cough Started:")

# === Submit Button ===
generate = st.button("🔍 Generate My Health Report")

# === Main Logic ===
if generate:
    if not name or not age.isdigit() or gender == "Select" or main_symptoms == "Select" or \
       not fever.replace('.', '', 1).isdigit() or mood == "Select" or not cough_days.isdigit():
        st.error("❌ Please ensure all fields are correctly filled.")
    else:
        age = int(age)
        fever = float(fever)
        cough_days = int(cough_days)

        with st.spinner("🔄 Analyzing your inputs..."):
            time.sleep(2)

        # === Risk Score Calculation ===
        risk_score = 0
        if main_symptoms == "fever":
            if fever > 102 or no_of_sick_days > 3:
                risk_score += 3
            elif age >= 60:
                risk_score += 2
            else:
                risk_score += 1

        elif main_symptoms == "cough":
            risk_score += 2 if cough_days >= 5 else 1

        elif main_symptoms == "fatigue":
            risk_score += 2 if age > 30 else 1

        elif main_symptoms == "headache":
            risk_score += 2 if fever > 100 else 1

        elif main_symptoms == "chest pain":
            risk_score += 3

        elif main_symptoms == "breathlessness":
            risk_score += 4

        if smoking_habit == "yes":
            risk_score += 2
        if sleep_hours < 6:
            risk_score += 1
        if mood in ["anxious", "irritable", "sad"]:
            risk_score += 1
        if pre_existing_conditions == "yes":
            risk_score += 2
        else:
            st.info("✅ No pre-existing conditions detected.")

        # === Health Report ===
        st.markdown("---")
        st.success(f"🧾 **Health Summary for {name.title()}**")

        if risk_score >= 7:
            st.error("🔴 **High Risk**: Please seek help from a healthcare provider immediately.")
        elif risk_score >= 4:
            st.warning("🟠 **Moderate Risk**: Consider consulting a healthcare professional.")
        else:
            st.success("✅ **Low Risk**: You're currently not showing concerning indicators.")

        st.markdown("---")
        st.markdown("### 📋 **Profile Summary**")
        st.write(f"**Name:** {name.title()}  ")
        st.write(f"**Age:** {age}, **Gender:** {gender.title()}, **City:** {city.title()}")
        st.write(f"**Symptom:** {main_symptoms}, **Fever:** {fever}°F, **Sick Days:** {no_of_sick_days}")
        st.write(f"**Smoker:** {smoking_habit}, **Sleep:** {sleep_hours} hrs, **Mood:** {mood}")
        st.write(f"**Pre-existing Conditions:** {pre_existing_conditions}")

        st.markdown("---")
        st.markdown("### 💡 **Personalized Health Advice**")
        if gender == "female" and age >= 45:
            st.write("- 🩺 Consider regular mammograms and bone density tests.")
        if gender == "male" and smoking_habit == "yes":
            st.write("- 🚭 Quit smoking and consider regular prostate check-ups.")
        if sleep_hours < 6:
            st.write("- 😴 Improve your sleep hygiene and aim for 7–8 hours of rest.")
        if mood == "anxious":
            st.write("- 🧘‍♀️ Try mindfulness, journaling, or therapy.")
        if pre_existing_conditions == "yes":
            st.write("- 🏥 Schedule regular follow-ups with your doctor.")
        else:
            st.write("- 🥗 Maintain a healthy lifestyle with exercise and a balanced diet.")

        st.markdown("---")
        st.markdown("### 🧠 **Mental Health Tips**")
        if mood == "calm":
            st.write("- 🌈 Keep it up! Enjoy your calm energy.")
        elif mood == "sad":
            st.write("- 💬 Talk to someone. Light exercise and company help.")
        elif mood == "anxious":
            st.write("- 🧘 Practice deep breathing and grounding exercises.")
        elif mood == "irritable":
            st.write("- 🎵 Take breaks. Try yoga, music or journaling to relax.")

        st.balloons()
        st.success(f"💚 Thank you for using the HealthCheck App. Stay safe and take care, {name.title()}!")
