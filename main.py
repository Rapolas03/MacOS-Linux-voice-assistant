import platform
from record import record_voice
from transcribe import transcribe_audio
from interpret import interpret_command
from excecute import execute_command
from text_to_speech import text_to_speech

def main():
    record_voice()
    text = transcribe_audio()
    print("You said:", text)

    command = interpret_command(text)
    print("AI interpreted command:", command)

    text_to_speech(f"The command interpreted is {command}")

    execute_command(command)

if __name__ == "__main__":
    main()

# pip install google-generativeai pyaudio SpeechRecognition pyttsx3