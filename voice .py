import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak something...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.write("Transcription: ", text)
        except sr.UnknownValueError:
            st.warning("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            st.error("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    st.title("Real-time Voice Transcription App")
    st.write("Speak into your microphone and the app will transcribe your speech.")

    if st.button("Start Transcription"):
        transcribe_speech()

if __name__ == "__main__":
    main()
