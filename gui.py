import tkinter as tk
from tkinter import ttk, messagebox
import base64
import urllib.parse
import pyperclip

def process(action):
    payload = entry.get()
    mode = mode_var.get()
    if not payload:
        messagebox.showerror("Error", "Please enter a payload.")
        return

    try:
        if action == "encode":
            if mode == "base64":
                result = base64.b64encode(payload.encode()).decode()
            elif mode == "hex":
                result = payload.encode().hex()
            elif mode == "url":
                result = urllib.parse.quote(payload)
        else:
            if mode == "base64":
                result = base64.b64decode(payload.encode()).decode()
            elif mode == "hex":
                result = bytes.fromhex(payload).decode()
            elif mode == "url":
                result = urllib.parse.unquote(payload)

        output_var.set(result)
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Payload Encoder/Decoder")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="Enter Payload:").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Label(root, text="Select Type:").pack()
mode_var = tk.StringVar(value="base64")
ttk.Combobox(root, textvariable=mode_var, values=["base64", "hex", "url"]).pack()

tk.Button(root, text="Encode", command=lambda: process("encode")).pack(pady=5)
tk.Button(root, text="Decode", command=lambda: process("decode")).pack(pady=5)

tk.Label(root, text="Output:").pack()
output_var = tk.StringVar()
tk.Entry(root, textvariable=output_var, width=50, state="readonly").pack()

root.mainloop()
