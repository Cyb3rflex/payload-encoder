import base64
import urllib.parse

def banner():
    print("""
  ____       _            _       ______             _
 |  _ \ __ _| | _____  __| | ___ |  ____|__  ___ ___| |__
 | |_) / _` | |/ / _ \/ _` |/ _ \|  _| / _ \/ __/ __| '_ \\
 |  __/ (_| |   <  __/ (_| | (_) | |__|  __/\__ \__ \ | | |
 |_|   \__,_|_|\_\___|\__,_|\___/|_____\___||___/___/_| |_|                                      
    """)

def encode_payload(payload):
    print("\n--- Encoded Formats ---")
    print("Base64:", base64.b64encode(payload.encode()).decode())
    print("Hex   :", payload.encode().hex())
    print("URL   :", urllib.parse.quote(payload))

def main():
    banner()
    payload = input("Enter your payload: ")
    encode_payload(payload)

if __name__ == "__main__":
    main()
