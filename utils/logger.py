import os
import time
from enum import Enum
from config.settings import LOGS_DIR

# ============================================================
# Log Levels
# ============================================================

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

# ============================================================
# Log Levels
# ============================================================

class LogOrigin(str, Enum):
    USER = "user"
    SCRIPT = "script"

# ============================================================
# Logger setup
# ============================================================

os.makedirs(LOGS_DIR, exist_ok=True)

START_TIME = time.strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(
    LOGS_DIR,
    f"{START_TIME}_autokeypress_log.txt"
)

# ============================================================
# Logger function
# ============================================================

def log_event(
    *,
    origin: LogOrigin = LogOrigin.SCRIPT,
    key: str | None = None,
    level: LogLevel = LogLevel.INFO
):
    """
    Write structured log entry.

    origin: 'user' | 'aq3d_autopresskey'
    key: key or action name
    level: LogLevel
    """

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log_line = (
        f"{timestamp} - "
        f"{{ origin: {origin.value}, level: {level.value}, key: {key} }}\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_line)

    print(log_line.strip())
