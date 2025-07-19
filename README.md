# Voice Command Interpreter

This project is a voice command interpreter that allows users to record voice commands, transcribe them into text, interpret the commands, and safely execute them. It also provides text-to-speech feedback for user convenience.

---

## Features
- **Voice Recording**: Record voice input using your system's microphone.
- **Audio Transcription**: Convert recorded audio to text using Google Speech Recognition.
- **Command Interpretation**: Interpret user commands locally or via Google Gemini API for enhanced functionality.
- **Command Execution**: Safely execute interpreted commands with built-in safety checks for dangerous commands.
- **Text-to-Speech**: Provide audible feedback for the interpreted commands.

---

## Requirements

- **Python**: Version 3.8 or higher
- **Dependencies**: See `requirements.txt` for a list of required Python packages.

### Python Packages
The following Python packages are required:
- `google-generativeai`
- `pyaudio`
- `SpeechRecognition`
- `pyttsx3`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone <repository-url>
cd <repository-name>
```

### Step 2: Set Up a Virtual Environment (Recommended)
It is best practice to use a virtual environment to manage your project's dependencies:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Google Gemini (Optional)
To use the Google Gemini API for command interpretation, set up the `GEMINI_API_KEY` environment variable:
```bash
export GEMINI_API_KEY="your-api-key-here"
```
If `GEMINI_API_KEY` is not set, the program will fall back to local command interpretation.

### Step 4: Run the Application
Run the main program to start the voice command interpreter:
```bash
python main.py
```

---

## How It Works
1. **Record Voice**: The system records your voice using the microphone.
2. **Transcribe Audio**: Converts the recorded audio into text.
3. **Interpret Command**: Analyzes the transcribed text and converts it into a safe command.
4. **Execute Command**: Runs the interpreted command while ensuring safety.
5. **Provide Feedback**: Reads the interpreted command aloud using text-to-speech.

---

## Example Commands
Here are some examples of commands you can speak:
- "Create a directory in the home folder called 'myfolder'."
- "List all files in the current directory."
- "Show me running processes."
- "Open Safari."

---

## Troubleshooting
- **Audio Issues**: Ensure your microphone is connected and properly configured.
- **Google Gemini Errors**: Check if your `GEMINI_API_KEY` is correctly set.
- **Dependency Problems**: Run `pip install -r requirements.txt` to ensure all dependencies are installed.

---

## Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.