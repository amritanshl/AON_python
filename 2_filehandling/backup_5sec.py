import os
import time
from datetime import datetime

# --- Start of the Training Script ---

# 1. We enter a 'While True' loop to keep the program running indefinitely.
while True:
    # 2. Capture the current system time object.
    now = datetime.now()

    # 3. Format the individual components for the Directory Hierarchy.
    # Note: These will be used to build the folder structure.
    year  = now.strftime("%Y")
    month = now.strftime("%m")
    day   = now.strftime("%d")
    hour  = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    # 4. Construct the Directory Path string using the required hierarchy.
    # We use os.path.join to ensure the slashes work on both Windows and Linux.
    target_dir = os.path.join(year, month, day, hour, minute)

    # 5. Technical Action: Create the directory tree.
    # 'exist_ok=True' prevents an error if the directory is already there.
    os.makedirs(target_dir, exist_ok=True)

    # 6. Format the filename based on the requirement: hdfc_ddMMyyyyhhmmss.txt
    file_name = now.strftime("hdfc_%d%m%Y%H%M%S.txt")

    # 7. Create the Full File Path (Folder Path + Filename)
    full_path = os.path.join(target_dir, file_name)

    # 8. Open the file in Write Mode ('w')
    with open(full_path, "w") as f:
        # Get the Absolute Path to include inside the file content.
        absolute_path = os.path.abspath(full_path)
        
        # Write the metadata into the file.
        f.write(f"Log Generation Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Physical Storage Path: {absolute_path}\n")
        f.write("Status: HDFC Transaction Log Placeholder\n")

    # 9. Technical Output: Confirmation in the console.
    print(f"Successfully created: {full_path}")

    # 10. Throttle the CPU: Wait for 5 seconds before the next iteration.
    # Without this, the program would create thousands of files per second.
    time.sleep(5)