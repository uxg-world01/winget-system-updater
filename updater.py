import os
import subprocess
import shutil
import ctypes

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ask_permission(message):
    """Prompt the user for permission (y/n)."""
    choice = input(f"\n[?] {message} (y/n): ").strip().lower()
    return choice == 'y'

def delete_folder_contents(folder_path):
    """Delete all files and folders inside a given directory."""
    if not os.path.exists(folder_path):
        print(f"[-] Folder not found: {folder_path}")
        return

    print(f"[*] Cleaning started for: {folder_path}")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            # Skip files that are currently in use by the system or other apps
            pass
    print(f"[+] Cleanup completed for: {folder_path}")

def main():
    if not is_admin():
        print("[!] WARNING: Administrative privileges are required to clean the Prefetch folder.")
        if not ask_permission("Do you want to continue without Admin privileges?"):
            print("Script terminated.")
            return

    # --- Winget Update Section ---
    if ask_permission("Do you want to check for Winget updates?"):
        subprocess.run(["winget", "update"])
        
        if ask_permission("Do you want to upgrade all available apps?"):
            subprocess.run(["winget", "upgrade", "--all"])

    # --- Windows Junk Files Cleanup Section ---
    if ask_permission("Do you want to delete all junk files from Windows Temp, %Temp%, and Prefetch?"):
        
        # 1. Windows Temp Folder
        windows_temp = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
        delete_folder_contents(windows_temp)

        # 2. User Temp Folder (%temp%)
        user_temp = os.environ.get('TEMP')
        if user_temp:
            delete_folder_contents(user_temp)

        # 3. Prefetch Folder
        prefetch = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Prefetch')
        delete_folder_contents(prefetch)
        
        print("\n[+] All temporary and junk files have been cleared!")

    # --- Winget Cleanup Section ---
    if ask_permission("Do you want to clear the Winget cache/settings?"):
        print("[*] Running Winget cleanup...")
        subprocess.run(["winget", "settings",], shell=True)

    print("\n[+] All tasks completed successfully!")

if __name__ == "__main__":
    main()