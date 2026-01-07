# AQ3D AutoKeyPress

Automated key press and mouse drag tool for **AQ3D**.  
This tool allows you to automatically press a configurable set of keys and move the mouse horizontally while holding a button, with hotkeys to start/stop actions. It includes a logging system with levels and origins.

---

## Features

- Auto key press for multiple keys (`1`, `2`, `3`, etc.)
- Auto mouse drag:
  - Moves the mouse horizontally left and right from the center
  - Holds the right mouse button while moving
- Hotkeys:
  - `F1` – Exit program
  - `F2` – Toggle auto key press
  - `F3` – Toggle mouse auto-drag
- Threaded architecture for simultaneous keyboard and mouse automation
- Logging system with timestamp, origin (`user` or `script`), and key pressed
- Configurable delays and key sets via `config/settings.py`

---

## Installation

**Requirements:** Python 3.10+ on Windows

1. Clone the repository:

```bash
git clone https://github.com/ikidon/aq3d_autopresskey.git
cd aq3d_autopresskey
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (cmd)
.\venv\Scripts\activate.bat
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python main.py
```

**Hotkeys while the program is running:**

- `F1` – Exit program
- `F2` – Toggle auto key press
- `F3` – Toggle mouse auto-drag

Logs are created automatically in the `logs/` folder. Each run generates a new log file with timestamp.

---

## Project Structure

```
aq3d_autopresskey/
│
├─ core/                  # Global state and thread management
├─ input/                 # Keyboard, mouse, and hotkey handlers
├─ utils/                 # Logging utilities
├─ config/                # Settings and configuration
├─ logs/                  # Automatically generated logs
├─ main.py                # Entry point
├─ requirements.txt       # Python dependencies
├─ setup.py               # Package setup for pip
└─ README.md              # Project documentation
```

---

## Logging Format

Logs follow the structure:

```
timestamp - { origin: user | script, key: key_pressed, level: INFO | WARNING | ERROR }
```

Example:

```
2026-01-07 08:15:30 - { origin: script, key: 1, level: INFO }
2026-01-07 08:15:35 - { origin: user, key: F2, level: INFO }
```

---

## Contributing

Feel free to fork the project and submit PRs. Please follow **modular coding** practices and **keep logging consistent**.

---

## License

This project is MIT licensed. See the [LICENSE](LICENSE) file for details.
