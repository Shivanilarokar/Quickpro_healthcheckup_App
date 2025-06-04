import time

# 1. User Profile

Name = input("Enter your name: ").title
Age = int(input("Enter your age: "))
Gender = input("Enter you gender: only male, female, or other): ").lower()
city = input("Enter your city: ")

#  Health inputs 
print("\n🤒 Select your main symptom from the list below:")
print("Options: fever, cough, fatigue, headache, chest pain, breathlessness")
main_symptoms = input("Enter your main symptoms: (choose from: fever, cough, fatigue, headache, chest pain, breathlessness): ").lower()                                                                                                                                      
Fever = float(input("Enter your body temperature in (F): ")) 
no_of_sick_days = int(input("No of days that you are sick: "))
smoking_habit= input("Do you smoke? (yes/no): ").lower() 
Sleep_hours = int(input("How many hours do you sleep? "))
Mood = input("How is your mood? (calm, anxious, sad, irritable): ").lower()
pre_exisiting_conditions = input("Do you have any pre-existing conditions? (yes/no): ").lower()
cough = int(input("No of days since you have a cough :" )) 
# Step 3: Simulated analysis
print("\n🔍 Processing your inputs...")
time.sleep(2)

### ⚙️ 3. Risk Scoring Logic
risk_score = 0
if main_symptoms == "fever":
    if Fever> 102  or no_of_sick_days >3:
        risk_score += 3
    elif Age >= 60 or Fever >= 102:
        risk_score += 2
if main_symptoms == "cough":
    if no_of_sick_days >=5 :
        risk_score += 2
if main_symptoms == "fatigue":
    if Age >30 :
     risk_score += 2
if main_symptoms == "headache":
    if Fever > 100:
        risk_score += 2 
if main_symptoms == "chest pain":
    risk_score += 3
elif main_symptoms == "breathlessness":
    risk_score += 4
elif smoking_habit == "yes":
    risk_score += 2 
elif Sleep_hours < 6:
    risk_score += 1 
elif Mood == "anxious" or Mood == "irritable" or Mood == "sad":
    risk_score += 1
if pre_exisiting_conditions == "yes":
    risk_score += 2
else:
    print("No pre-existing conditions detected.")



print("\n🔍 Processing your inputs...")
time.sleep(2)


# #  Health Risk Result
# Based on total score, print a health warning:

# 0–3 → 🟢 Low Risk
# 4–6 → 🟠 Moderate Risk
# 7+ → 🔴 High Risk 


if risk_score >0 and risk_score <= 3:
    print("\n🟢 Low Risk: Your health appears stable. Maintain a healthy lifestyle and monitor your symptoms.")  
elif risk_score > 4 and risk_score <= 6:
    print("\n🟠 Moderate Risk: You should consider consulting a healthcare professional for further evaluation.")
elif risk_score >= 7:
    print("\n🔴 High Risk: Immediate medical attention is recommended. Please seek help from a healthcare provider.")

# 4. Summary of User Profile and Health Risk
print("\n📋 Summary of Your Profile:")


# Personalised health advice.

if Gender == "female" and Age >= 45:
    print("Health Screening: Consider regular mammograms and bone density tests.") 
elif Gender == "male" and smoking_habit == "yes":
    print("Quit smoking to reduce the risk of lung disease and cancer. Consider regular prostate screenings.")
elif Sleep_hours < 6:
    print("Sleep Hygiene: Aim for 7-8 hours of quality sleep per night. Consider relaxation techniques before bedtime.")
elif Mood == "anxious":
    print("Mental Health: Consider mindfulness practices or speaking with a mental health professional to manage anxiety.")
elif pre_exisiting_conditions == "yes":
    print("Pre-existing Conditions: Regular check-ups with your healthcare provider are essential to manage your health effectively.")
else:
    print("General Health Advice: Maintain a balanced diet, regular exercise, and stay hydrated. Regular health check-ups are recommended.")

# Mental Health tips
print("\n🧠 Mental Health Tips:")

if Mood == "calm":
    print("Keep up the good work! Continue engaging in activities that promote relaxation and well-being & maintain a positive mindset.")
elif Mood =="sad":
    print("Consider talking to a friend or a mental health professional. Engaging in physical activity can also help improve your mood.")
elif Mood == "anxious":
    print("Practice deep breathing & box brreathing exercises manage anxiety. Consider speaking with a mental health professional if needed.")
elif Mood == "irritable":  
    print("Take breaks and practice stress-relief techniques such as meditation or yoga.")