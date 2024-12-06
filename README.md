# WiFi Password Tester

A Python-based tool for scanning available Wi-Fi networks and testing passwords from a predefined or user-specified list. This tool uses the `pywifi` library to automate the process of verifying Wi-Fi network security.

> **Disclaimer:** This tool is intended for educational purposes and ethical security testing on networks you own or have explicit permission to test. Unauthorized access to networks is illegal.

---

## Features
- **Scan Networks:** Lists all available Wi-Fi networks in range.
- **Password Testing:** Attempts to connect to a selected network using passwords from a file.
- **Custom Password Files:** Supports user-specified password files for testing.

---

## Prerequisites
- Python 3.6 or later
- A device with Wi-Fi support
- `pywifi` library installed

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/wifi-password-tester.git
    cd wifi-password-tester
    ```

2. Install the required library:
    ```bash
    pip install pywifi
    ```

---

## Usage

1. **Run the script** to scan for available Wi-Fi networks:
    ```bash
    python main-tester.py
    ```

2. **Select a network** from the displayed list by entering its number.

3. **Provide a password file** (if `passwords.txt` is not in the directory):
    - The password file should be a text file with one password per line.

4. **View the results**:
    - If a valid password is found, it will be displayed.
    - If none of the passwords work, the script will notify you.

---

## Example Workflow

1. Place your password file (`passwords.txt`) in the same directory as the script, or specify a custom path when prompted.
2. Run the script:
    ```bash
    python main-tester.py
    ```
3. The script will:
    - Scan for available Wi-Fi networks.
    - List all unique SSIDs.
    - Allow you to select a network to test.
    - Test passwords from your file sequentially.
4. The result will indicate whether a valid password was found.

---

## Notes
- **Scanning Time:** The script waits for 2 seconds after scanning networks to allow results to populate. You can adjust this in the `list_available_networks()` function if needed.
- **Password Testing:** The script disconnects from any active network before testing new passwords.

---

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Arikatakur/WiFi-Password-Tester/tree/main?tab=MIT-1-ov-file) file for details.

---

## Disclaimer
This tool is strictly for use on networks you own or have explicit permission to test. Unauthorized use is illegal and may result in severe consequences.
