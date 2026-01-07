import threading
from input.keyboard import auto_key_loop
from input.mouse import mouse_drag_loop

# ============================
# Thread management
# ============================

THREADS = []  # Stores references to threads, in case you need to control them later.


def start_threads():
    """
    Start background threads for auto key press and mouse drag.
    Threads are daemonized so they exit automatically when the program stops.
    """
    global THREADS

    # Auto key press thread
    key_thread = threading.Thread(target=auto_key_loop, daemon=True, name="AutoKeyThread")
    key_thread.start()
    THREADS.append(key_thread)

    # Mouse drag thread
    mouse_thread = threading.Thread(target=mouse_drag_loop, daemon=True, name="MouseDragThread")
    mouse_thread.start()
    THREADS.append(mouse_thread)
