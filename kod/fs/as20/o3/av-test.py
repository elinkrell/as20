import os
import platform
import time

# This test code will NOT damage the computer

system = platform.system()

if system == "Windows":
    # Continue with Windows-specific logic
    print("Windows detected. Script execution continues...")

elif system == "Linux":
    print("Linux detected. This script is intended for Windows only.")
    exit()

elif system == "Darwin":
    print("macOS detected. This script is intended for Windows only.")
    exit()

else:
    print(f"Unknown operating system ({system}). This script is intended for Windows only. Aborting execution.")
    exit()

eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" # EICAR testfile string
desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop') # Creates desktop path and file path
file_path = os.path.join(desktop_path, "eicar_testfile.txt")

# Write EICAR string to file
try:
    with open(file_path, "w") as f:
        f.write(eicar_str)
    print(f"EICAR testfile created: {file_path}")
except Exception as e:
    print(f"Error creating EICAR testfile: {e}")
    exit(1)
    
print("[...] Wait for antivirus to scan the file...")
time.sleep(5)  # Antivirus will scan the file in 5 seconds

if not os.path.exists(file_path):
    print("EICAR testfile does not exist.")
    print("EICAR testfile has been deleted, likely by AV/EDR.")
    print("Your antivirus works correctly.")
    exit(0)

try: 
    with open(file_path, "r") as f:
        content = f.read()
    if content == eicar_str:
        print("EICAR testfile is still present and complete.")
        print("Your antivirus failed to detect the EICAR testfile.")
    else:
        print("EICAR testfile content has been changed.")
        print("Your antivirus might have partially detected the EICAR testfile.")
except Exception as e:
    print(f"[...]Could not read the EICAR testfile: {e}")
    print("Your antivirus might have prevented operation of the EICAR testfile.")
    print("Your antivirus is working correctly.")
