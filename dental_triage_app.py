import streamlit as st

# Set up the app title and description
st.title("Comprehensive Dental Triage Tool")
st.write("""
This triage tool helps you determine the urgency of your dental symptoms based on various factors. 
Please provide as much accurate information as possible to help classify the severity of your condition.
""")

# Section for user inputs
st.header("Patient Information")

# Demographic information
age = st.slider("Age", 1, 100, 30)
gender = st.radio("Gender", ["Male", "Female", "Other"])

# Symptom details
st.subheader("Symptoms")

pain_level = st.slider("Pain level (1 = no pain, 10 = severe pain)", 1, 10, 5)
swelling = st.radio("Do you have facial swelling?", ["No", "Mild", "Severe"])
bleeding = st.radio("Is there any bleeding in your mouth?", ["Yes", "No"])
toothache_duration = st.selectbox("How long have you had a toothache?", 
                                  ["Less than a day", "1-3 days", "3-7 days", "More than a week", "No toothache"])

# Specific dental issues
st.subheader("Specific Dental Conditions")
broken_tooth = st.radio("Do you have a broken or chipped tooth?", ["Yes", "No"])
loose_teeth = st.radio("Are any of your teeth loose?", ["Yes", "No"])
fever = st.radio("Do you have a fever?", ["Yes", "No"])
bad_breath = st.radio("Do you have persistent bad breath?", ["Yes", "No"])
gum_pain = st.radio("Do you have any gum pain?", ["Yes", "No"])
difficulty_eating = st.radio("Do you have difficulty eating due to dental pain?", ["Yes", "No"])
trauma = st.radio("Did you experience trauma (e.g., fall, hit) to your teeth or mouth?", ["Yes", "No"])

# Extra details
st.subheader("Other Health Conditions")
diabetes = st.radio("Do you have diabetes?", ["Yes", "No"])
immune_system = st.radio("Do you have a weakened immune system?", ["Yes", "No"])

# Triage logic to classify severity
def triage(age, pain_level, swelling, bleeding, toothache_duration, broken_tooth, loose_teeth,
           fever, bad_breath, gum_pain, difficulty_eating, trauma, diabetes, immune_system):
    # Emergency cases
    if trauma == "Yes" or (swelling == "Severe" and fever == "Yes"):
        return "Emergency: You need to see a dentist or go to the emergency room immediately due to possible infection or trauma."
    
    if bleeding == "Yes" and (pain_level >= 8 or broken_tooth == "Yes"):
        return "Emergency: Bleeding along with severe pain or a broken tooth requires immediate attention."

    # Urgent cases
    if loose_teeth == "Yes" or difficulty_eating == "Yes":
        return "Urgent: Contact your dentist as soon as possible. Loose teeth or difficulty eating may require prompt attention."
    
    if fever == "Yes" and gum_pain == "Yes":
        return "Urgent: You might have an infection that needs to be addressed quickly."

    if broken_tooth == "Yes":
        return "Urgent: A broken tooth can lead to more serious problems if not treated soon."

    if toothache_duration in ["1-3 days", "3-7 days", "More than a week"]:
        return "Urgent: A persistent toothache lasting several days should be evaluated by a dentist soon."

    # Routine cases
    if bad_breath == "Yes" and gum_pain == "Yes":
        return "Routine: This might be due to gum disease or another minor issue. Book a regular appointment."

    if toothache_duration == "Less than a day" and pain_level <= 4:
        return "Routine: Monitor the pain, but it doesn't seem to require immediate attention."

    # Health conditions raising concern
    if diabetes == "Yes" or immune_system == "Yes":
        return "You should visit your dentist for routine check-ups, as these conditions may increase your risk of dental issues."

    return "Routine: There doesn't seem to be an immediate cause for concern, but visit your dentist if symptoms persist."

# Button for submitting data and performing triage
if st.button("Triage Me"):
    result = triage(age, pain_level, swelling, bleeding, toothache_duration, broken_tooth, loose_teeth,
                    fever, bad_breath, gum_pain, difficulty_eating, trauma, diabetes, immune_system)
    st.subheader("Triage Result:")
    st.write(result)

# Add educational content about common dental emergencies
st.subheader("Common Dental Emergencies and How to Respond")

st.write("""
- **Tooth Abscess**: A pocket of pus that forms due to infection. It requires immediate care.
- **Fractured or Displaced Teeth**: Trauma or injury can cause this, requiring urgent care.
- **Severe Toothache**: Can indicate infection or serious dental decay.
- **Uncontrolled Bleeding**: Bleeding after trauma or surgery must be addressed immediately.
- **Facial Swelling with Fever**: May indicate infection spreading beyond the tooth and needs emergency care.
""")

# Footer
st.write("""
---
This is a tool to help guide your decision on the urgency of your dental issues. However, it does not replace professional medical advice. 
Please see a healthcare professional for an accurate diagnosis and appropriate treatment.
""")
