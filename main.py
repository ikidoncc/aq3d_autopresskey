from pynput.keyboard import Listener
from core.hotkeys import on_press
from core.threads import start_threads
from utils.logger import log_event, LogOrigin, LogLevel

def main():
    start_threads()
    log_event(level=LogLevel.INFO)
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
