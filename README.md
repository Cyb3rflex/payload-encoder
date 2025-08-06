# 🔐 Payload Encoder

A simple yet powerful Python tool for encoding and decoding payloads in multiple formats — built for cybersecurity researchers, ethical hackers, and developers.

---

## 🚀 Features

- Encode and decode payloads in:
  - Base64
  - Hexadecimal
  - URL Encoding
- Easy-to-use Command Line Interface (CLI)
- One-click clipboard copy option
- Graphical User Interface (GUI) using Tkinter (PC use)
- GitHub-ready and Termux-compatible

---

## 🧰 Requirements

- Python 3
- `pyperclip` (for clipboard copy)
- `tkinter` (for GUI - optional, use on PC or VNC)

Install dependencies:
```bash
pip install pyperclip
```
---

🖥️ CLI Usage

▶️ Encode a Payload

```bash
python encoder.py encode base64 "ls -la"
```

# 🔁 Decode a Payload

```bash
python encoder.py decode base64 "bHMgLWxhCg=="
```

# 📋 With Clipboard Copy

```bash
python encoder.py encode hex "rm -rf /" --copy
```

---

# 🖼️ GUI Usage

> Tkinter GUI doesn't work natively in Termux. Run it on PC or VNC.

  ```bash
   python gui.py
   ```
  >You’ll get a window interface to input payloads, select encoding type, and get results with clipboard copy support.


---

## 📂 Project Structure

```bash
payload-encoder/
├── encoder.py       # Main CLI script
├── gui.py           # GUI application using Tkinter
└── README.md        # This file
```

---

## 💡 Future Features (Planned)

 - Encode/decode from files

 - Auto-detect payload type

 - Export results to a file

 - Android APK GUI version



---

## 🧑‍💻 Author

> @Cyb3rflex
- Termux-powered security tools developer 💻📱🔐


---

## ⚠️ Disclaimer

This tool is intended for educational and ethical use only. Do not use it for illegal activities.


---

## ⭐ Star This Repo

If you find this project helpful, consider giving it a ⭐ on GitHub. It really helps!


