import time

# 1. User Profile
print("\n📝 Welcome to the HealthCheck App!\nPlease provide the following details:")

name = input("Enter your name: ").title()

age = input("Enter your age: ").strip()
if not age.isdigit():
    print("❌ Invalid input. Age must be a number.")
    exit()
age = int(age)

gender = input("Enter your gender (male/female/other): ").lower().strip()
if gender not in ["male", "female", "other"]:
    print("❌ Invalid gender. Please enter 'male', 'female', or 'other'.")
    exit()

city = input("Enter your city: ").title().strip()

# 2. Health Inputs
print("\n🤒 Select your main symptom from the list below:")
print("Options: fever, cough, fatigue, headache, chest pain, breathlessness")
main_symptoms = input("Enter your main symptom: ").lower().strip()

fever = input("Enter your body temperature in Fahrenheit (F): ")
if not fever.replace('.', '', 1).isdigit():
    print("❌ Invalid input. Temperature must be a number.")
    exit()
fever = float(fever)

no_of_sick_days = input("Number of days you've been sick: ")
if not no_of_sick_days.isdigit():
    print("❌ Invalid input. Sick days must be a number.")
    exit()
no_of_sick_days = int(no_of_sick_days)

smoking_habit = input("Do you smoke? (yes/no): ").lower().strip()
if smoking_habit not in ["yes", "no"]:
    print("❌ Invalid input. Please enter 'yes' or 'no'.")
    exit()

sleep_hours = input("How many hours do you sleep per night? ")
if not sleep_hours.isdigit():
    print("❌ Invalid input. Sleep hours must be a number.")
    exit()
sleep_hours = int(sleep_hours)

mood = input("How is your mood? (calm, anxious, sad, irritable): ").lower().strip()
if mood not in ["calm", "anxious", "sad", "irritable"]:
    print("❌ Invalid input. Choose mood from the list.")
    exit()

pre_existing_conditions = input("Do you have any pre-existing conditions? (yes/no): ").lower().strip()
if pre_existing_conditions not in ["yes", "no"]:
    print("❌ Invalid input. Please enter 'yes' or 'no'.")
    exit()

cough_days = input("Number of days since you have had a cough: ")
if not cough_days.isdigit():
    print("❌ Invalid input. Cough days must be a number.")
    exit()
cough_days = int(cough_days)

# 3. Simulated analysis
print("\n🔍 Processing your inputs...")
time.sleep(2)

# 4. Risk Scoring Logic
risk_score = 0

if main_symptoms == "fever":
    if fever > 102 or no_of_sick_days > 3:
        risk_score += 3
    elif age >= 60:
        risk_score += 2
    else:
        risk_score += 1

elif main_symptoms == "cough":
    if cough_days >= 5:
        risk_score += 2
    else:
        risk_score += 1

elif main_symptoms == "fatigue":
    if age > 30:
        risk_score += 2
    else:
        risk_score += 1

elif main_symptoms == "headache":
    if fever > 100:
        risk_score += 2
    else:
        risk_score += 1

elif main_symptoms == "chest pain":
    risk_score += 3

elif main_symptoms == "breathlessness":
    risk_score += 4

# Additional Risk Factors
if smoking_habit == "yes":
    risk_score += 2

if sleep_hours < 6:
    risk_score += 1

if mood in ["anxious", "irritable", "sad"]:
    risk_score += 1

if pre_existing_conditions == "yes":
    risk_score += 2
else:
    print("✅ No pre-existing conditions detected.")

# 5. Output Results
print("\n🧾 Health Summary for", name + ":")
time.sleep(2)

if risk_score >= 7:
    print("\n🔴 High Risk: Immediate medical attention is recommended. Please seek help from a healthcare provider.")
elif risk_score >= 4:
    print("\n🟠 Moderate Risk: You should consider consulting a healthcare professional for further evaluation.")   
else:
    print("\n✅ You're currently not showing concerning risk indicators. Stay healthy!")

# Summary
print("\n📋 Summary of Your Profile:")
print(f"Name: {name}, Age: {age}, Gender: {gender.title()}, City: {city}")
print(f"Main Symptom: {main_symptoms}, Temperature: {fever}°F, Sick for {no_of_sick_days} days")
print(f"Smoker: {smoking_habit}, Sleep Hours: {sleep_hours}, Mood: {mood}")
print(f"Pre-existing Conditions: {pre_existing_conditions}")

# Health Advice
print("\n💡 Personalized Health Advice:")
if gender == "female" and age >= 45:
    print("- Consider regular mammograms and bone density tests.")
if gender == "male" and smoking_habit == "yes":
    print("- Quit smoking to reduce lung disease and cancer risk. Consider regular prostate check-ups.")
if sleep_hours < 6:
    print("- Try to get 7–8 hours of sleep. Practice good sleep hygiene.")
if mood == "anxious":
    print("- Try mindfulness, journaling, or consult a therapist to manage anxiety.")
if pre_existing_conditions == "yes":
    print("- Schedule regular follow-ups with your healthcare provider.")
else:
    print("- Maintain a balanced diet, exercise regularly, and hydrate well.")

# Mental Health Tips
print("\n🧠 Mental Health Tips:")
if mood == "calm":
    print("- Keep it up! Continue activities that help you feel relaxed and happy.")
elif mood == "sad":
    print("- Talk to a friend or professional. Exercise and social connection can help uplift mood.")
elif mood == "anxious":
    print("- Practice deep breathing or box breathing. Consider therapy for support.")
elif mood == "irritable":
    print("- Take short breaks during the day and try stress relief techniques like yoga or meditation.")

print(f"\n💚 Thank you for using the HealthCheck App. Stay safe and take care {name}!")
