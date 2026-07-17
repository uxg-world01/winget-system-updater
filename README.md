# Windows Cleanup & Winget Maintenance Tool

A lightweight Python utility for **Windows system maintenance** that helps keep your PC clean and up to date. The script interactively asks for permission before performing each action, making it safe and user-friendly.

---

# Features

* ✅ Interactive Yes/No confirmation before every task
* ✅ Checks for Administrator privileges
* ✅ Updates Winget package information
* ✅ Upgrades installed applications using Winget
* ✅ Cleans Windows Temp folder
* ✅ Cleans User Temp (%TEMP%) folder
* ✅ Cleans Windows Prefetch folder
* ✅ Resets Winget settings (optional)
* ✅ Skips locked or in-use files automatically
* ✅ Simple terminal interface
* ✅ No external Python libraries required

---

# What This Script Does

The program performs the following maintenance tasks:

### 1. Administrator Check

Before accessing protected folders like:

* `C:\Windows\Temp`
* `C:\Windows\Prefetch`

the script checks whether it is running as Administrator.

If not, it warns the user and asks whether to continue.

---

### 2. Winget Update

Optionally runs:

```powershell
winget update
```

This refreshes the Winget package database.

---

### 3. Upgrade Installed Applications

Optionally runs:

```powershell
winget upgrade --all
```

This updates every installed application that has a newer version available through Winget.

Examples:

* Visual Studio Code
* Python
* Git
* Docker Desktop
* Microsoft PowerToys
* Windows Terminal

---

### 4. Windows Temporary File Cleanup

Deletes all files inside:

```
C:\Windows\Temp
```

These files are temporary installation or system cache files that Windows no longer needs.

---

### 5. User Temporary Folder Cleanup

Deletes everything inside:

```
%TEMP%
```

Example:

```
C:\Users\<username>\AppData\Local\Temp
```

This folder commonly contains:

* Installer leftovers
* Application cache
* Crash logs
* Temporary browser data

---

### 6. Prefetch Cleanup

Deletes contents of:

```
C:\Windows\Prefetch
```

Prefetch stores application startup information.

Windows automatically recreates these files whenever programs are opened again.

---

### 7. Winget Settings Reset

Optionally runs:

```powershell
winget settings --reset
```

This restores Winget settings to their default configuration.

---

# Requirements

* Windows 10 or Windows 11
* Python 3.8+
* Winget installed
* Administrator privileges (recommended)

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/windows-cleanup-tool.git
```

Move into the project:

```bash
cd windows-cleanup-tool
```

No dependencies are required.

---

# Usage

Run the script:

```bash
python cleanup.py
```

The program will ask before every operation.

Example:

```
Do you want to check Winget updates? (y/n)

Do you want to upgrade all apps? (y/n)

Do you want to clean temporary files? (y/n)

Do you want to reset Winget settings? (y/n)
```

---

# Project Structure

```
Windows-Cleanup-Tool/

│
├── cleanup.py
├── README.md
└── LICENSE
```

---

# Safety

The script **only deletes the contents** of the following folders:

* Windows Temp
* User Temp
* Prefetch

It **does not delete the folders themselves**.

Files currently being used by Windows or other applications are skipped automatically.

---

# Notes

* Running as Administrator is recommended.
* Windows will automatically recreate Temp and Prefetch files when needed.
* Resetting Winget settings does **not** uninstall applications.

---

# Example Workflow

```
Start Script
      │
      ▼
Check Administrator
      │
      ▼
Ask User
      │
      ├── Winget Update
      │
      ├── Upgrade Apps
      │
      ├── Clean Windows Temp
      │
      ├── Clean User Temp
      │
      ├── Clean Prefetch
      │
      └── Reset Winget Settings
      │
      ▼
Finish
```

---

# Future Improvements

* Disk Cleanup integration (`cleanmgr`)
* Windows Update automation
* Recycle Bin cleanup
* Browser cache cleanup
* DNS cache flush
* Event Log cleanup
* Startup program manager
* Scheduled automatic maintenance
* Disk usage report
* Colored terminal output
* Logging system
* Progress bars

---

# Disclaimer

This project is intended for **system maintenance and cleanup only**. While it deletes only temporary files and caches, use it at your own discretion. Running the script with Administrator privileges is recommended for full functionality.

---

# License

This project is released under the **MIT License**.

Feel free to modify, distribute, and use it for personal or commercial purposes.
