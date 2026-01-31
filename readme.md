# 📂 SmartFiles Organizer

> **Intelligent File Automation for Windows**
> Keeps your PC organized effortlessly. Sorts downloads and cleans junk files automatically.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🚀 What does it do?

This script acts as a "digital butler" running silently in the background:

1.  **Real-Time Organizer:**
    * Watches your **Downloads** folder 24/7.
    * Instantly moves files to categorized folders (`Documents`, `Images`, `Installers`, etc.).
    * Handles duplicates automatically (appends timestamp if file exists).
    * Smartly ignores incomplete downloads (`.crdownload`, `.part`) to prevent errors.

2.  **Auto-Maintenance (System Cleaner):**
    * Once a week (every 7 days), it performs a deep clean:
        * 🗑️ Empties the **Recycle Bin** silently.
        * 🧹 Cleans junk files from the Windows **%TEMP%** folder.

3.  **Zero Configuration:**
    * Fully portable. It detects its own location and manages logs locally.

---

## 🛠️ Quick Installation

### 1. Environment Setup
Make sure **Python** is installed. Open this folder in your terminal (`cmd` or `PowerShell`) and run:

```powershell
# Create virtual environment (recommended)
python -m venv venv

# Activate environment
.\venv\Scripts\activate

# Install the required dependency
pip install watchdog
2. Running (Stealth Mode)
To run the script without keeping a terminal window open, use the included run_smartfiles.bat file.

Just double-click the .bat file.

Nothing will appear on screen (this is intentional).

Check organizer.log to confirm startup: SERVICE: Organizador iniciado.

3. Start on Boot
To make SmartFiles run automatically when you turn on your PC:

Create a Shortcut of the run_smartfiles.bat file.

Press Win + R, type shell:startup and hit Enter.

Move the shortcut into that folder.

⚙️ Configuration (Optional)
The script works out-of-the-box, but you can edit organizer.py to customize:

DEST_MAP: Define where each file type goes.

Ex: ".pdf": "Documents/PDFs"

CLEANUP_INTERVAL: How often to clean system junk in seconds (Default: 604800 = 7 days).

📝 Logs & Debugging
All activity is recorded in organizer.log inside the script folder.

MOVED: File successfully sorted.

SYSTEM: Junk cleanup executed.

ERROR: Something went wrong (e.g., file locked by another program).

🛑 How to Stop
Since the script runs in background (stealth mode), to stop it:

Open Task Manager (Ctrl + Shift + Esc).

Go to the Details tab.

End the pythonw.exe task.

Author: Rúben