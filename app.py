import json
import streamlit as st

# Load the JSON data
with open('bot.json', 'r') as file:
    medical_data = json.load(file)


# Function to find medical condition by name and symptoms
def find_condition(name, symptoms):
    for condition in medical_data['medical_issues']:
        if condition['name'].lower() == name.lower():
            # Check if all provided symptoms match
            matched_symptoms = set(symptoms).intersection(set(condition['symptoms']))
            if matched_symptoms:
                return condition
    return None


# Function to get user input and provide medication and treatment
def chat_with_user():
    st.title("Medical Chatbot")
    st.write("🤖 Hi there! I'm here to help you with your medical concerns.")

    # Collect user input
    condition_name = st.text_input("What's bothering you? (e.g., headache, fever)", key="condition_name")
    symptoms_input = st.text_input("Can you describe the symptoms you're experiencing? (separated by commas)",
                                   key="symptoms_input")

    if condition_name.lower() == 'exit':
        st.write("Goodbye! Feel free to come back anytime.")
    elif condition_name and symptoms_input:
        symptoms = [symptom.strip() for symptom in symptoms_input.split(',')]
        condition = find_condition(condition_name, symptoms)

        if condition:
            st.write(f"\n🔍 I found information on '{condition['name']}'.")
            st.write("Here's what matches your description:")
            for symptom in symptoms:
                if symptom in condition['symptoms']:
                    st.write(f" - {symptom}")

            st.write("\n💊 Medication and Treatments:")
            for treatment in condition['treatments']:
                st.write(f"\nType: {treatment['type']}")
                st.write("Options:")
                for option in treatment['options']:
                    st.write(f" - {option}")
        else:
            st.write("❌ I couldn't find information on that condition or your symptoms don't match.")


# Run the function to interact with user
chat_with_user()
