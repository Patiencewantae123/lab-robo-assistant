import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
speech_engine = pyttsx3.init()

# Set the speech rate (optional)
speech_engine.setProperty('rate', 150)

def speak(text):
    """Convert text to speech."""
    speech_engine.say(text)
    speech_engine.runAndWait()

def listen():
    """Listen for voice input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            # Convert speech to text using Google Speech Recognition
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return ""

def main():
    """Main function for the PIONEER INNOVATION LAB Assistant."""
    speak("Hello! Welcome to the Pioneer Innovation Lab. I specialize in Artificial Intelligence, Cybersecurity, Smart Agriculture, Mobile Development, and Smart Websites. How can I assist you today?")
    
    while True:
        command = listen()

        # General greeting
        if "hello" in command:
            speak("Hi! How can I help you with Artificial Intelligence, Cybersecurity, Smart Agriculture, Mobile Development, or Smart Websites?")

        # Artificial Intelligence related command
        elif "artificial intelligence" in command or "ai" in command:
            speak("Artificial Intelligence is revolutionizing industries. Do you want to learn more about AI or see some AI projects?")
        
        # Cybersecurity related command
        elif "cybersecurity" in command:
            speak("Cybersecurity is essential for protecting information. Do you want to know about cybersecurity best practices or tools?")
        
        # Smart Agriculture related command
        elif "smart agriculture" in command or "agriculture" in command:
            speak("Smart Agriculture uses technology to improve farming. Are you interested in learning more about sensors, automation, or data analytics in agriculture?")
        
        # Mobile Development related command
        elif "mobile development" in command or "mobile apps" in command:
            speak("Mobile Development involves creating apps for mobile platforms. Do you want to explore development tools or learn about frameworks like Flutter or React Native?")
        
        # Smart Websites related command
        elif "smart websites" in command or "web development" in command:
            speak("Smart websites use AI to improve user experience. Do you want to learn more about dynamic websites or AI integration in web development?")
        
        # Open Google
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        
        # Search on Wikipedia
        elif "tell me about" in command:
            topic = command.replace("tell me about", "")
            speak(f"Searching for {topic} on Wikipedia.")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple entries for this topic. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")
        
        # Time command
        elif "time" in command:
            import time
            current_time = time.strftime('%I:%M %p')
            speak(f"The current time is {current_time}")
        
        # Exit or Goodbye command
        elif "exit" in command or "goodbye" in command:
            speak("Goodbye! Have a productive day at the Pioneer Innovation Lab.")
            break
        
        # Unrecognized commands
        else:
            speak("I'm sorry, I don't understand that command. Could you repeat or ask about Artificial Intelligence, Cybersecurity, Smart Agriculture, Mobile Development, or Smart Websites?")

if __name__ == "__main__":
    main()
