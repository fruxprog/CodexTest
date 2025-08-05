import threading
import tkinter as tk
from tkinter import ttk

from ping_utils import ping


class PingApp(ttk.Frame):
    """Simple GUI application for IPv4 and IPv6 ping."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=10)
        master.title("Ping GUI")
        master.geometry("420x300")
        self.pack(fill="both", expand=True)

        self.address_var = tk.StringVar(value="8.8.8.8")

        entry = ttk.Entry(self, textvariable=self.address_var)
        entry.pack(fill="x", pady=(0, 5))

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=(0, 5))

        ttk.Button(btn_frame, text="Ping IPv4", command=lambda: self.start_ping(4)).pack(
            side="left", expand=True, fill="x"
        )
        ttk.Button(btn_frame, text="Ping IPv6", command=lambda: self.start_ping(6)).pack(
            side="left", expand=True, fill="x"
        )

        self.log = tk.Text(self, state="disabled", height=10)
        self.log.pack(fill="both", expand=True)

    # GUI helpers
    def append_log(self, message: str) -> None:
        self.log.configure(state="normal")
        self.log.insert("end", message + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    # Ping handling
    def start_ping(self, version: int) -> None:
        address = self.address_var.get().strip()
        threading.Thread(target=self.run_ping, args=(address, version), daemon=True).start()

    def run_ping(self, address: str, version: int) -> None:
        self.append_log(f"Pinging {address} (IPv{version})...")
        result = ping(address, version)
        if result["success"]:
            elapsed = f"{result['elapsed_ms']} ms" if result["elapsed_ms"] is not None else "?"
            self.append_log(f"Success ({elapsed})")
        else:
            self.append_log("Failed")
        if result.get("output"):
            self.append_log(result["output"])
        if result.get("error"):
            self.append_log(result["error"])


def main() -> None:
    root = tk.Tk()
    PingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
