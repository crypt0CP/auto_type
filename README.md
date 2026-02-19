# auto_type
# ⌨️ auto_type

A simple Python automation script using **PyAutoGUI** that automatically types a specific text and presses Enter multiple times.

⚠️ This script controls your keyboard automatically. Use carefully.

---

## 📌 What This Script Does

The script:

- Types `zswd`
- Presses `Enter`
- Repeats the process 1000 times
- Runs very fast (0.01 second delay between actions)

---

## 🛠 Requirements

- Python 3.x
- PyAutoGUI library

---

## 📦 Installation

### 1️⃣ Install Python (if not installed)

Download from: https://www.python.org/downloads/

Check version:

```
python --version
```

---

### 2️⃣ Clone the Repository

```
git clone https://github.com/crypt0CP/auto_type.git
```

---

### 3️⃣ Navigate to Project Folder

```
cd auto_type
```

---

### 4️⃣ Install Required Library

```
pip install pyautogui
```

---

## ▶️ How to Use

1. Open the application where you want the text to be typed  
   (Example: Notepad, VS Code, Browser chat, etc.)

2. Click inside the text field so the cursor becomes active.

3. Run the script:

```
python auto_type.py
```

4. The script will immediately start typing automatically.

---

## 🧠 Script Code

```python
import pyautogui
import time

pyautogui.FAILSAFE = False

for i in range(0, 1000):
    time.sleep(0.01)
    pyautogui.typewrite('zswd')
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.01)
```

---

## ⚙️ How to Edit the Script

### 🔹 Change the Text

Modify this line:

```python
pyautogui.typewrite('zswd')
```

Example:

```python
pyautogui.typewrite('Hello World')
```

---

### 🔹 Change Number of Repetitions

Modify:

```python
for i in range(0, 1000):
```

Example (run 20 times):

```python
for i in range(0, 20):
```

---

### 🔹 Change Typing Speed

Modify sleep value:

```python
time.sleep(0.01)
```

Example (slower typing):

```python
time.sleep(0.5)
```

---

### 🔹 Enable Emergency Stop (Highly Recommended)

Change:

```python
pyautogui.FAILSAFE = False
```

To:

```python
pyautogui.FAILSAFE = True
```

Now moving your mouse to the **top-left corner** of the screen will instantly stop the script.

---

## ⚠️ Important Warning

- Do NOT use this script for spamming.
- Do NOT use in online games or illegal activities.
- It types in any active window — always test carefully.
- Start with small loop numbers (like 5 or 10) for safety.

---

## 🚀 Future Improvements

- Add user input for custom text
- Add start delay countdown (e.g., 5 seconds before typing starts)
- Add GUI interface
- Add hotkey to stop script
- Add random delay for human-like typing

---

## 👨‍💻 Author

crypt0CP
---

## 📜 Disclaimer

This project is for educational and automation practice purposes only.  
Use responsibly.
