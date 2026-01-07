import ctypes
import time
from config.settings import MOUSE_MOVE_DISTANCE, MOUSE_STEP, MOUSE_DELAY
from core import state

# ============================
# Windows Mouse Constants
# ============================
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_ABSOLUTE = 0x8000

# ============================
# Windows User32
# ============================
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Precompute absolute center coordinates
ABS_CENTER_X = int((screen_width // 2) / screen_width * 65535)
ABS_CENTER_Y = int((screen_height // 2) / screen_height * 65535)


# ============================
# Low-level mouse functions
# ============================
def mouse_right_down():
    """Press and hold the right mouse button."""
    user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def mouse_right_up():
    """Release the right mouse button."""
    user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def mouse_move(dx: int, dy: int):
    """Move the mouse relative to the current position."""
    user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)


def mouse_to_center():
    """Move the mouse to the center of the screen using absolute coordinates."""
    user32.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, ABS_CENTER_X, ABS_CENTER_Y, 0, 0)


# ============================
# Mouse drag loop
# ============================
def mouse_drag_loop():
    """
    Moves the mouse horizontally back and forth while holding the right button:
    1. Moves to screen center
    2. Moves right then left repeatedly
    """
    directions = [1, -1, -1, 1]  # +1 = right, -1 = left

    while not state.stop_program:
        if not state.mouse_running:
            time.sleep(0.1)
            continue

        mouse_right_down()
        try:
            mouse_to_center()

            while state.mouse_running and not state.stop_program:
                for direction in directions:
                    move_mouse_steps(direction)
        finally:
            mouse_right_up()


def move_mouse_steps(direction: int):
    """
    Move the mouse a given distance in small steps in a horizontal direction.

    :param direction: +1 for right, -1 for left
    """
    steps = MOUSE_MOVE_DISTANCE // MOUSE_STEP
    for _ in range(steps):
        if not state.mouse_running or state.stop_program:
            break
        mouse_move(MOUSE_STEP * direction, 0)
        time.sleep(MOUSE_DELAY)
