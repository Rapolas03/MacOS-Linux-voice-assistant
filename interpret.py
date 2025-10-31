import platform
import google.generativeai as genai
import os
import re

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None
    print(" GEMINI_API_KEY not found. Using local fallback only.")

def get_system_context():
    """Get system-specific context"""
    system = platform.system()
    if system == "Linux":
        return "You are a Linux assistant. Convert this request to a safe bash command. Return ONLY the command, no explanations or markdown formatting:"
    elif system == "Darwin":  # macOS
        return "You are a macOS assistant. Convert this request to a safe bash command. Return ONLY the command, no explanations or markdown formatting:"
    elif system == "Windows":
        return "You are a Windows assistant. Convert this request to a safe PowerShell or CMD command. Return ONLY the command, no explanations or markdown formatting:"
    return "Convert this request to a safe command. Return ONLY the command:"

def interpret_with_gemini(user_input):
    """Use Google Gemini for command interpretation"""
    if not model:
        return None
        
    try:
        prompt = f"{get_system_context()}\n\nUser request: {user_input}"
        response = model.generate_content(prompt)
        
        # Clean up response (remove markdown formatting if present)
        result = response.text.strip()
        result = result.replace('```bash', '').replace('```', '').strip()
        return result
        
    except Exception as e:
        print(f"Gemini API error: {e}")
        return None

def local_fallback(user_input):
    """Enhanced local fallback for common commands"""
    system = platform.system()
    user_lower = user_input.lower().strip()
    
    print(f"🔄 Processing locally for {system}")
    print(f"🔍 Input: '{user_input}'")
    
    # Extract directory name from common patterns
    def extract_directory_name(text):
        """Extract directory name from text"""
        # Look for "called X", "named X", or just the last word
        patterns = [
            r"called\s+(\w+)",
            r"named\s+(\w+)", 
            r"folder\s+(\w+)",
            r"directory\s+(\w+)\s*$"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        
        # If no specific pattern, try to get the last word
        words = text.split()
        if words:
            return words[-1]
        return "newfolder"
    
    # macOS/Linux commands
    if system in ["Darwin", "Linux"]:
        # Directory creation patterns
        if re.search(r"creat.*director", user_lower) or re.search(r"make.*director", user_lower) or re.search(r"creat.*folder", user_lower):
            dir_name = extract_directory_name(user_lower)
            
            if "home" in user_lower:
                command = f"mkdir ~/{dir_name}"
                print(f"Matched home directory creation: {command}")
                return command
            else:
                command = f"mkdir {dir_name}"
                print(f" Matched directory creation: {command}")
                return command
        
        # Other common patterns
        patterns = {
            # File operations
            r"list.*files?.*current.*director": "ls -la",
            r"list.*files?": "ls -l",
            r"show.*files?": "ls -la", 
            r"^dir$": "ls -la",
            
            # Disk operations
            r"disk.*usage": "df -h",
            r"free.*space": "df -h",
            r"storage.*space": "df -h",
            
            # Find operations
            r"find.*python.*files?": "find . -name '*.py'",
            r"find.*\.py": "find . -name '*.py'",
            r"search.*python": "find . -name '*.py'",
            r"find.*all.*files": "find . -type f",
            
            # Process operations
            r"running.*process": "ps aux",
            r"process.*list": "ps aux",
            r"show.*process": "ps aux",
            
            # Navigation
            r"current.*director": "pwd",
            r"where.*am.*i": "pwd",
            r"go.*home": "cd ~",
            
            # System info
            r"system.*info": "uname -a",
            r"os.*version": "sw_vers" if system == "Darwin" else "lsb_release -a",
            
            # File operations
            r"copy.*file": "cp",
            r"move.*file": "mv",
            r"delete.*file": "rm",
            r"remove.*file": "rm",
            
            # Text operations
            r"show.*content": "cat",
            r"read.*file": "cat",
            r"edit.*file": "nano",


            # Opening operations

            r"open.*safari": "open /Applications/Safari.app",
        }
        
        # Try other patterns
        for pattern, command in patterns.items():
            if re.search(pattern, user_lower):
                print(f" Matched pattern: {command}")
                return command
    
    # Windows commands
    else:
        if re.search(r"creat.*director", user_lower):
            dir_name = extract_directory_name(user_lower)
            command = f"mkdir {dir_name}"
            print(f" Matched Windows directory creation: {command}")
            return command
            
        patterns = {
            r"list.*files?": "dir",
            r"show.*files?": "dir",
            r"disk.*usage": "dir /-c",
            r"free.*space": "dir /-c",
            r"find.*python.*files?": "dir *.py /s",
            r"running.*process": "tasklist",
            r"process.*list": "tasklist",
            r"current.*director": "cd",
            r"copy.*file": "copy",
            r"move.*file": "move",
            r"delete.*file": "del",
        }
        
        for pattern, command in patterns.items():
            if re.search(pattern, user_lower):
                print(f" Matched pattern: {command}")
                return command
    
    # Default fallback
    print(" No specific pattern matched, using default")
    if system in ["Darwin", "Linux"]:
        return "ls -la"
    else:
        return "dir"

def interpret_command(user_input):
    """Main function that tries Gemini first, then falls back to local commands"""
    print(f"🔍 Interpreting: {user_input}")
    
    # Try Gemini first
    if model:
        result = interpret_with_gemini(user_input)
        if result and not result.startswith("X"):
            print("Using Gemini API")
            return result
        else:
            print(" Gemini API failed, using local fallback")
    else:
        print(" Gemini not available, using local fallback")
    
    # Use local fallback
    print(" Using local fallback")
    return local_fallback(user_input)

# Test function
if __name__ == "__main__":
    # Test the specific command that failed
    test_commands = [
        "can you create a directory in the home folder called hello",
        "create a folder named test",
        "make a directory called myproject",
        "list all files",
        "show running processes"
    ]
    
    for cmd in test_commands:
        print("=" * 50)
        result = interpret_command(cmd)
        print(f"Final result: {result}")

