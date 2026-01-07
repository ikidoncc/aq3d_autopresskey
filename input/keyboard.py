import time
from pynput.keyboard import Controller
from config.settings import KEYS_TO_PRESS, KEY_DELAY
from core import state
from utils.logger import log_event, LogLevel

keyboard = Controller()


def auto_key_loop():
    """
    Continuously presses configured keys while keys_running is True.
    Stops when stop_program is True.
    """
    while not state.stop_program:
        if not state.keys_running:
            time.sleep(0.1)
            continue

        for key in KEYS_TO_PRESS:
            if not state.keys_running or state.stop_program:
                break

            keyboard.press(key)
            keyboard.release(key)
            log_event(key=key, level=LogLevel.INFO)
            time.sleep(KEY_DELAY)
