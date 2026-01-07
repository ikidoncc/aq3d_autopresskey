from pynput.keyboard import Key
from core import state
from utils.logger import log_event, LogLevel, LogOrigin

# Mapping hotkeys to actions
HOTKEY_ACTIONS = {
    Key.f1: "exit_program",
    Key.f2: "toggle_keys",
    Key.f3: "toggle_mouse",
}

def on_press(key):
    """
    Handles hotkey presses:
    F1 - Exit program
    F2 - Toggle auto key press
    F3 - Toggle mouse auto-drag
    """
    action = HOTKEY_ACTIONS.get(key)

    if action == "exit_program":
        state.keys_running = False
        state.mouse_running = False
        state.stop_program = True
        log_event(origin=LogOrigin.USER, key=key, level=LogLevel.INFO)
        return False  # stops the listener

    elif action == "toggle_keys":
        state.keys_running = not state.keys_running
        log_event(origin=LogOrigin.USER, key=key, level=LogLevel.INFO)

    elif action == "toggle_mouse":
        state.mouse_running = not state.mouse_running
        log_event(origin=LogOrigin.USER, key=key, level=LogLevel.INFO)
