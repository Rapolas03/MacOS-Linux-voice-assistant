import pyttsx3
import platform

def text_to_speech(text):
    """Convert text to speech"""
    try:
        engine = pyttsx3.init()
        
        # voice 
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # first available 
        
        # Speed of speech
        engine.setProperty('rate', 150)  
        # Volume level (0.0 to 1.0)
        engine.setProperty('volume', 0.8)  
        
        print(f"🔊 Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")
        print(f"📝 Would have said: {text}")

