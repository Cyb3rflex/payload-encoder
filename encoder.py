import base64
import urllib.parse
import argparse
import pyperclip

def encode(payload, mode):
    if mode == 'base64':
        return base64.b64encode(payload.encode()).decode()
    elif mode == 'hex':
        return payload.encode().hex()
    elif mode == 'url':
        return urllib.parse.quote(payload)
    else:
        raise ValueError("Unsupported encoding type.")

def decode(payload, mode):
    if mode == 'base64':
        return base64.b64decode(payload.encode()).decode()
    elif mode == 'hex':
        return bytes.fromhex(payload).decode()
    elif mode == 'url':
        return urllib.parse.unquote(payload)
    else:
        raise ValueError("Unsupported decoding type.")

def banner():
    print(r"""
  ____       _            _       ______             _
 |  _ \ __ _| | _____  __| | ___ |  ____|__  ___ ___| |__
 | |_) / _` | |/ / _ \/ _` |/ _ \|  _| / _ \/ __/ __| '_ \\
 |  __/ (_| |   <  __/ (_| | (_) | |__|  __/\__ \__ \ | | |
 |_|   \__,_|_|\_\___|\__,_|\___/|_____\___||___/___/_| |_|

    """)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="Encode or decode payloads easily.")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose mode: encode or decode")
    parser.add_argument("type", choices=["base64", "hex", "url"], help="Encoding/decoding type")
    parser.add_argument("payload", help="The string to encode or decode")
    parser.add_argument("--copy", action="store_true", help="Copy result to clipboard")

    args = parser.parse_args()

    try:
        if args.mode == "encode":
            result = encode(args.payload, args.type)
        else:
            result = decode(args.payload, args.type)
        
        print(f"\nResult:\n{result}")

        if args.copy:
            import os
            os.system(f'echo "{result}" | termux-clipboard-set') 
            print("\n✅ Copied to clipboard!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
