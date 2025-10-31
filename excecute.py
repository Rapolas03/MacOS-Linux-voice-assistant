import subprocess
import platform

def execute_command(command):
    """Execute the interpreted command"""
    if not command or command.startswith("x"):
        print("x No valid command to execute")
        return
    
    print(f" Executing: {command}")
    
    # Safety check
    dangerous_patterns = ['rm -rf /', 'sudo rm -rf', 'format', 'del /f /q', '> /dev/null 2>&1']
    if any(pattern in command.lower() for pattern in dangerous_patterns):
        print(" Dangerous command detected! Execution blocked.")
        return
    
    try:
        # Execute command and capture output
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=30  # 30 second timeout
        )
        
        if result.stdout:
            print(" Output:")
            print(result.stdout)
        
        if result.stderr:
            print(" Errors:")
            print(result.stderr)
            
        if result.returncode != 0:
            print(f" Command failed with exit code: {result.returncode}")
        else:
            print(" Command executed successfully")
            
    except subprocess.TimeoutExpired:
        print(" Command timed out after 30 seconds")
    except Exception as e:
        print(f" Execution error: {e}")
