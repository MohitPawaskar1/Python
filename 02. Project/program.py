import pyautogui
import pyperclip
import time

# Function to simulate Ctrl + C (copy)
def copy_text():
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)  # Wait for clipboard to update
    return pyperclip.paste()

# Step 1: Click on the icon at (1075, 1058)
pyautogui.click(1075, 1058)
time.sleep(1)  # Wait for UI to respond

# Step 2: Drag to select text (from 692, 230 to 1880, 987)
pyautogui.moveTo(692, 230)  # Move to start position
pyautogui.mouseDown()  # Press left mouse button
pyautogui.moveTo(1880, 987, duration=1)  # Drag to end position
pyautogui.mouseUp()  # Release mouse button

time.sleep(0.5)  # Small delay to ensure selection

# Step 3: Copy the selected text
selected_text = copy_text()

# Step 4: Print the copied text
print(f"Copied Text: {selected_text}")
