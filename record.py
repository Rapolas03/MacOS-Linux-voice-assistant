import pyaudio
import wave
import threading
import time

def record_voice(filename="voice_input.wav", duration=5):
    """Record voice input for specified duration"""
    print("🎤 Recording... (Press Ctrl+C to stop early)")
    
    # Audio settings
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    
    # Start recording
    stream = audio.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)
    
    frames = []
    
    try:
        for i in range(0, int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK)
            frames.append(data)
            if i % 10 == 0:  # Print progress
                print(".", end="", flush=True)
    except KeyboardInterrupt:
        print("\n🛑 Recording stopped early")
    
    print(f"\n✅ Recording complete: {filename}")
    
    # Stop and close stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # Save recording
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    return filename
