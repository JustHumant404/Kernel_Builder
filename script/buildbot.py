import asyncio
import os
import sys
import textwrap
from telethon import TelegramClient

API_ID = 27075271
API_HASH = "f1809f81c3bea88dcd8efda067189539"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
MESSAGE_THREAD_ID = os.environ.get("MESSAGE_THREAD_ID")
KERNELVER = os.environ.get("KERNELVER")
PATHKERNEL = os.environ.get("PATHKERNEL")
KSUVER = os.environ.get("KSUVERSION")
DRIVERKSU = os.environ.get("DRIVERKSU")
MSG_TEMPLATE = textwrap.dedent(r"""
**New Build Published!**
```Kernel Information
KernelVer: {kernelversion}
DriverKSU: {driverksu} ({ksuver])
SUSFS ඞ: v1.5.9
```
""").strip()

def get_caption():
    msg = MSG_TEMPLATE.format(
        kernelversion=KERNELVER,
        driverksu=DRIVERKSU,
        ksuver=KSUVER,
    )
    if len(msg) > 1024:
        return f"{kernelversion}"
    return msg

def check_environ():
    global CHAT_ID, MESSAGE_THREAD_ID
    if BOT_TOKEN is None:
        print("[-] Invalid BOT_TOKEN")
        exit(1)
    if CHAT_ID is None:
        print("[-] Invalid CHAT_ID")
        exit(1)
    else:
        try:
            CHAT_ID = int(CHAT_ID)
        except:
            pass
    if MESSAGE_THREAD_ID is not None and MESSAGE_THREAD_ID != "":
        try:
            MESSAGE_THREAD_ID = int(MESSAGE_THREAD_ID)
        except:
            print("[-] Invaild MESSAGE_THREAD_ID")
            exit(1)
    else:
        MESSAGE_THREAD_ID = None
    get_versions()

async def main():
    print("[+] Uploading to telegram")
    check_environ()
    files = sys.argv[1:]
    print("[+] Files:", files)
    if len(files) <= 0:
        print("[-] No files to upload")
        exit(1)
    print("[+] Logging in Telegram with bot")
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    session_dir = os.path.join(script_dir, "ksubot")
    async with await TelegramClient(session=session_dir, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN) as bot:
        caption = [""] * len(files)
        caption[-1] = get_caption()
        print("[+] Caption: ")
        print("---")
        print(caption)
        print("---")
        print("[+] Sending")
        await bot.send_file(entity=CHAT_ID, file=files, caption=caption, reply_to=MESSAGE_THREAD_ID, parse_mode="MarkdownV2")
        print("[+] Done!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"[-] An error occurred: {e}")
