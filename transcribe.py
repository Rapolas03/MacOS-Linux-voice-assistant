import speech_recognition as sr
import os

def transcribe_audio(filename="voice_input.wav"):
    """Transcribe audio file to text using Google Speech Recognition"""
    if not os.path.exists(filename):
        return "❌ Audio file not found"
    
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(filename) as source:
            print("🔄 Transcribing audio...")
            audio = recognizer.record(source)
        
        
        text = recognizer.recognize_google(audio)
        print("✅ Transcription complete")
        return text
        
    except sr.UnknownValueError:
        return "❌ Could not understand audio"
    except sr.RequestError as e:
        return f"❌ Speech recognition error: {e}"
    except Exception as e:
        return f"❌ Error: {e}"

