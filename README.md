# Ping GUI Test App

This repository contains a small Python application with a graphical user
interface for sending IPv4 and IPv6 ping requests.  Results are displayed in a
scrollable log window.

## Requirements

- Python 3.10+
- Tkinter (usually included with Python)
- `ping` command available in the system
- Optional: [`pytest`](https://pytest.org/) for running tests

## Usage

Run the GUI:

```bash
python ping_gui.py
```

Enter a host name or IP address and click **Ping IPv4** or **Ping IPv6** to see
results in the log window.

## Running Tests

To verify the ping helper functions without starting the GUI, run:

```bash
pytest -q
```

The tests ping the local host for both IPv4 and IPv6. The IPv6 test is skipped
if no IPv6 stack is available.

## Project Structure

- `ping_utils.py` – helper function for executing ping commands
- `ping_gui.py` – Tkinter user interface
- `tests/` – basic unit tests
- `requirements.txt` – optional development dependency
