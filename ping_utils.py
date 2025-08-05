import platform
import subprocess
from typing import Dict, Optional


def ping(address: str, version: int = 4, count: int = 1, timeout: int = 2) -> Dict[str, Optional[str]]:
    """Ping an address using IPv4 or IPv6.

    Parameters
    ----------
    address: str
        Hostname or IP address to ping.
    version: int
        IP version (4 or 6).
    count: int
        Number of echo requests to send.
    timeout: int
        Time to wait for a response in seconds (Linux/Mac only).

    Returns
    -------
    dict
        Mapping containing ``success`` (bool), ``output`` (str),
        ``elapsed_ms`` (float or None) and ``error`` (str or None).
    """
    if version not in (4, 6):
        raise ValueError("version must be 4 or 6")

    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", f"-{version}", "-n", str(count), address]
    else:
        # Linux and macOS
        cmd = ["ping", f"-{version}", "-c", str(count), "-W", str(timeout), address]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        success = result.returncode == 0
    except Exception as exc:
        return {"success": False, "output": "", "elapsed_ms": None, "error": str(exc)}

    elapsed_ms = None
    if success:
        import re

        match = re.search(r"time[=<]([\d\.]+) ?ms", result.stdout)
        if match:
            elapsed_ms = float(match.group(1))
        else:
            match = re.search(r"Average = ([\d\.]+)ms", result.stdout)
            if match:
                elapsed_ms = float(match.group(1))

    return {
        "success": success,
        "output": result.stdout.strip(),
        "elapsed_ms": elapsed_ms,
        "error": None,
    }
