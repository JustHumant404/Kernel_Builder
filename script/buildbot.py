import asyncio
import os
import sys
from telethon import TelegramClient

API_ID = 27075271
API_HASH = "f1809f81c3bea88dcd8efda067189539"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
MESSAGE_THREAD_ID = os.environ.get("MESSAGE_THREAD_ID")
KPM = os.environ.get("KPM")
PATHKERNEL = os.environ.get("PATHKERNEL")
MSG_TEMPLATE = """
**New Build Published!**
```kernelver: {kernelversion}
KsuVersion: {Ksuver}
KPM: {kpm}
```
""".strip()


def get_caption():
    msg = MSG_TEMPLATE.format(
        kernelversion=kernelversion,
        kpm=KPM,
        Ksuver=ksuver,
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

def get_kernel_versions():
    version=""
    patchlevel=""
    sublevel=""

    try:
        with open("Makefile",'r') as file:
            for line in file:
                if line.startswith("VERSION"):
                    version = line.split('=')[1].strip()
                elif line.startswith("PATCHLEVEL"):
                    patchlevel = line.split('=')[1].strip()
                elif line.startswith("SUBLEVEL"):
                    sublevel = line.split('=')[1].strip()
                elif line.startswith("#"): # skip comments
                    continue
                else:
                    break
    except FileNotFoundError:
        raise
    return f"{version}.{patchlevel}.{sublevel}"

def get_versions():
    global kernelversion,ksuver
    if not PATHKERNEL:
        raise EnvironmentError("Environment variable 'PATHKERNEL' is not set or is empty.")
    current_work=os.getcwd()
    os.chdir(os.path.join(current_work, PATHKERNEL, "common"))
    kernelversion=get_kernel_versions()
    os.chdir(os.getcwd()+"/../KernelSU")
    ksuver=os.popen("echo $(git describe --tags $(git rev-list --tags --max-count=1))-$(git rev-parse --short HEAD)@$(git branch --show-current)").read().strip()
    os.chdir(current_work)

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
        await bot.send_file(entity=CHAT_ID, file=files, caption=caption, reply_to=MESSAGE_THREAD_ID, parse_mode="markdown")
        print("[+] Done!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"[-] An error occurred: {e}")
