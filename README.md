# Russian Roulette: Linux Uninstall Edition

## ⚠️ Warning: Dangerous Script! ⚠️

**This script is extremely dangerous and should not be executed on any real system. It is intended for educational purposes only and demonstrates high-risk operations that can result in irreversible data loss and system failure.**

### Script Overview

This script simulates a game of "Russian Roulette" by attempting to delete the root directory (`/`) of a Linux system. If the root deletion fails due to an incorrect password, the script will randomly delete a file from a commonly used directory.

### Key Features:
- **Password Verification**: The script prompts the user to enter the admin password.
- **Randomized Deletion**: A 1 in 6 chance per round of deleting the root directory.
- **Retry Mechanism**: Up to 3 attempts to enter the correct password before proceeding to delete a random file.
- **Automatic Directory Selection**: Automatically selects a directory (`~/`, `/var/log`, or `/tmp`) to delete a file from if the root deletion fails.

### ⚠️ Important Warnings:
1. **Data Loss**: Running this script will result in data loss. Deleting the root directory or random files can make your system unusable.
2. **System Failure**: Deleting the root directory (`/`) will cause complete system failure.
3. **Educational Use Only**: This script should only be used for educational purposes and never on any important or production systems.
4. **No Liability**: The authors and contributors are not liable for any damage caused by the misuse of this script.

### Disclaimer
**Use this script at your own risk.** Understand the consequences of running such high-risk operations. Always test scripts in a safe and controlled environment.

### Example Usage:

1. Clone the repository.
2. Navigate to the script directory.
3. Run the script with caution: `python russian_roulette.py`

---

**Remember:**
**Think before you run. This script is dangerous.**

