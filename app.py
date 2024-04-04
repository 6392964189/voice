import streamlit as st
import speech_recognition as sr

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio).lower()
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")

# Function to provide answers based on user's query
def get_answer(question):
    # Define a dictionary mapping questions to answers
    answer_dict = {
        "what is the capital of India?": "The capital of India is New Delhi.",
        "what is the population of India?": "The population of India is approximately 1.3 billion.",
        "what is the currency of India?": "The currency of India is the Indian Rupee (INR).",
        # Add more questions and answers as needed
    }
    # Check if the question exists in the answer dictionary
    if question in answer_dict:
        return answer_dict[question]
    else:
        return "Sorry, I don't have an answer to that question."

# Main function
def main():
    st.title("Indian States Information App")
    st.write("Welcome to the Indian States Information App!")
    st.markdown("---")
    
    button_counter = 0  # Counter for generating unique button keys
    
    while True:
        button_counter += 1
        key = f"speak_button_{button_counter}"
        st.write("Press the button and ask your question:")
        command = st.button("Speak", key=key)
        
        if command:
            question = recognize_speech()
            if question:
                st.write("You asked:", question)
                answer = get_answer(question)
                st.info("Answer:")
                st.write(answer)

if __name__ == "__main__":
    main()
