# 📂 SmartFiles Organizer

> **Intelligent File Automation for Windows**
> Keeps your PC organized effortlessly. Sorts downloads and cleans junk files automatically.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🚀 Key Features

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

3.  **Zero Config:**
    * No Python installation required. Works right out of the box.

---

## 📦 Installation (Easy Mode)

### 1. Download
Go to the **Releases** section of this repository and download the latest ZIP file (e.g., `SmartFiles_v1.0.zip`).
* Inside, you will find the `organizer.exe` file.
* Extract it to a permanent folder (e.g., `Documents/SmartFiles`).

### 2. Run
Just double-click `organizer.exe`.
* **Note:** The program runs in "stealth mode" (background), so **no window will appear**.
* To confirm it is running, check if an `organizer.log` file was created in the same folder.

> ⚠️ **Antivirus Warning (False Positive):**
> Since this is an open-source tool without a paid digital certificate, Windows Defender might incorrectly flag it as suspicious.
> * If Windows blocks execution, click **"More Info"** -> **"Run Anyway"**.

---

## 🤖 Start on Boot
To make SmartFiles run automatically when you turn on your PC:

1.  Right-click `organizer.exe` and select **Create Shortcut**.
2.  Press `Win + R`, type `shell:startup`, and hit Enter.
3.  Move the shortcut into the folder that opens.

---

## ⚙️ For Developers (Source Code)
If you want to modify destination folders or logic, use the Python version:

1.  Clone the repo.
2.  Install dependencies: `pip install watchdog`.
3.  Edit `organizer.py`.
4.  Run with `python organizer.py`.

---

## 📝 Logs
All activity is recorded in `organizer.log` inside the script folder.
* `MOVED`: File successfully sorted.
* `SYSTEM`: Junk cleanup executed.

## 🛑 How to Stop
Since the script runs in the background, to stop it:
1.  Open **Task Manager** (`Ctrl + Shift + Esc`).
2.  Go to the **Details** tab.
3.  End the task **`organizer.exe`** (or `pythonw.exe` if running from source).

---
**Author:** Rúben