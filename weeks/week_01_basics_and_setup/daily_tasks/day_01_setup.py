"""
Day 1: Environment Setup Verification 🚀
---------------------------------------
Welcome to Day 1! This script verifies that your local environment is correctly 
configured to run Python 3 and displays details about your current system setup.

Task Instructions:
1. Open this file in your editor (e.g., VS Code).
2. Activate your virtual environment (.venv).
3. Run the script from your terminal:
   python day_01_setup.py
"""

import sys
import os
import platform

def verify_setup():
    print("=" * 45)
    print("🐍 Welcome to the 90 Days of Python Challenge! 🐍")
    print("=" * 45)
    
    # 1. Check Python Version
    version = sys.version_info
    print(f"✔️  Python Version Detected: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠️  Warning: It is recommended to use Python 3.8 or higher.")
    else:
        print("🎉 Your Python version is perfectly up to date!")
        
    # 2. Check System Info
    print(f"✔️  Operating System: {platform.system()} {platform.release()} ({platform.machine()})")
    
    # 3. Check virtual environment status
    is_venv = 'VIRTUAL_ENV' in os.environ
    if is_venv:
        print(f"✔️  Virtual Environment: Active (Path: {os.environ['VIRTUAL_ENV']})")
    else:
        print("❌ Virtual Environment: Inactive. (Recommended: Create and activate a .venv!)")
        
    print("=" * 45)
    print("Congratulations! Your developer tools are ready. You are set for Day 2!")
    print("=" * 45)

if __name__ == "__main__":
    verify_setup()
