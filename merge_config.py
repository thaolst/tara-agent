#!/usr/bin/env python3
"""Ghep cau hinh Tara Agent vao OpenClaw config hien tai.

Hoat dong tren macOS, Linux, va Windows.
Tu dong kiem tra prerequisite truoc khi ghi config."""

import json
import os
import sys
import platform
import subprocess
import re
import getpass

SYSTEM = platform.system()


# ----- PREREQ CHECKS -----

def check_node():
    """Kiem tra Node.js co duoc cai dat khong."""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"  \u2705 Node.js: {result.stdout.strip()}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("  \u274c Khong tim thay Node.js. Can cai Node.js (https://nodejs.org).")
    return False


def check_openclaw():
    """Kiem tra OpenClaw co duoc cai dat khong."""
    try:
        result = subprocess.run(["openclaw", "--version"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            print(f"  \u2705 OpenClaw: {version}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("  \u274c Khong tim thay OpenClaw. Chay: npm install -g openclaw@latest")
    return False


def check_python():
    """Kiem tra Python 3 (phong than)."""
    print(f"  \u2705 Python 3: {sys.version.split()[0]}")
    return True


def check_config_exists():
    """Kiem tra openclaw.json da duoc tao chua."""
    cfg = os.path.expanduser("~/.openclaw/openclaw.json")
    if os.path.exists(cfg):
        print(f"  \u2705 Config ton tai: {cfg}")
        return True
    print(f"  \u274c Chua co config tai: {cfg}")
    print("     Chay 'openclaw onboard' truoc de tao config mac dinh.")
    return False


def prompt_bot_token():
    """Hoi nguoi dung nhap botToken (an khi go). Uu tien env var $BOT_TOKEN."""
    env_token = os.environ.get("BOT_TOKEN", "").strip()
    if env_token:
        print("\n  \U0001f4e6 Doc BOT_TOKEN tu environment variable")
        if validate_token(env_token):
            return env_token
        print("  \u26a0\ufe0f BOT_TOKEN trong env khong hop le, se hoi lai.")

    print("")
    print("  === TELEGRAM BOT TOKEN ===")
    print("  Tao bot tai @BotFather (Telegram) -> /newbot")
    print("  Token se duoc an khi go (khong hien tren man hinh).")
    try:
        token = getpass.getpass("  Bot token: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n  \u26a0\ufe0f Khong nhap token. Dung lai.")
        sys.exit(1)

    if not token:
        print("  \u26a0\ufe0f Token trong. Dung lai.")
        print("     Chay lai script va nhap token hop le.")
        return None
    if not validate_token(token):
        print("  \u26a0\ufe0f Token co ve khong dung dinh dang (can co ':' o giua).")
        retry = input("     Tiep tuc voi token nay? (y/N): ").strip().lower()
        if retry != "y":
            print("  Dung lai. Chay lai script khi co token dung.")
            sys.exit(1)
    return token


def validate_token(token):
    """Kiem tra token co dung dang <so>:<chuoi> khong."""
    return bool(re.match(r"^\d+:[\w\-_]+$", token))


# ----- MAIN LOGIC -----

def get_workspace_path():
    """Tra ve path workspace phu hop voi OS."""
    return os.path.normpath(os.path.expanduser("~/.openclaw/workspace-social"))


def main():
    print("")
    print("  ===================================")
    print("    Tara Agent - Merge Config")
    print("    OS: " + SYSTEM)
    print("  ===================================")
    print("")

    # Step 1: Check prerequisites (khong block, chi canh bao)
    print("  \U0001f4cb Kiem moi truong...")
    all_ok = True
    all_ok &= check_python()
    all_ok &= check_node()
    all_ok &= check_openclaw()
    all_ok &= check_config_exists()
    print("")

    if not all_ok:
        print("  \u26a0\ufe0f Thieu mot so thanh phan. Khac phuc roi chay lai.")
        cont = input("     Tiep tuc merge? (y/N): ").strip().lower()
        if cont != "y":
            print("  Dung lai.")
            sys.exit(1)
        print("")

    # Step 2: Doc config hien tai
    config_path = os.path.expanduser("~/.openclaw/openclaw.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    workspace_path = get_workspace_path()

    # Step 3: Hoi botToken
    bot_token = prompt_bot_token()

    # Step 4: Merge channels
    if "channels" not in config:
        config["channels"] = {}
    config["channels"]["telegram"] = {
        "enabled": True,
        "botToken": bot_token or "123456:ABC-def_ghi",
        "dmPolicy": "open",
        "allowFrom": ["*"],
        "groupPolicy": "disabled"
    }
    if bot_token:
        print("  \u2705 Da them Telegram channel (voi token that)")
    else:
        print("  \u26a0\ufe0f Da them Telegram channel (token gia - can sua sau)")

    # Step 5: Merge social agent
    if "agents" not in config:
        config["agents"] = {"list": []}
    existing_ids = [a.get("id") for a in config["agents"].get("list", [])]

    if "social" not in existing_ids:
        social_agent = {
            "id": "social",
            "name": "Tara Social Agent",
            "workspace": workspace_path,
            "identity": {"emoji": "\U0001f4e2"},
            "subagents": {"allowAgents": []}
        }
        config["agents"]["list"].append(social_agent)
        print(f"  \u2705 Da them social agent (workspace: {workspace_path})")
    else:
        print("  \u2139\ufe0f Social agent da ton tai, bo qua")

    # Step 6: Merge bindings
    if "bindings" not in config:
        config["bindings"] = []
    existing_bindings = [b for b in config["bindings"] if b.get("agentId") == "social"]
    if not existing_bindings:
        config["bindings"].append({
            "match": {
                "channel": "telegram",
                "peer": {"kind": "dm", "id": "*"}
            },
            "agentId": "social"
        })
        print("  \u2705 Da them bindings cho Telegram DM -> social agent")
    else:
        print("  \u2139\ufe0f Bindings da ton tai, bo qua")

    # Step 7: Tao workspace + SOUL.md
    os.makedirs(workspace_path, exist_ok=True)
    soul_path = os.path.join(workspace_path, "SOUL.md")
    if not os.path.exists(soul_path):
        with open(soul_path, "w", encoding="utf-8") as f:
            f.write("""# SOUL.md - Tara Social Agent

Bạn là social agent. Nhiệm vụ: soạn và đăng bài LinkedIn, Facebook, Threads.

## Quy trình
1. Người dùng gửi lệnh: "soạn bài linkedin", "soạn bài facebook", "soạn bài threads"
2. Bạn soạn draft theo style từng nền tảng
3. Gửi draft lại, hỏi: "Duyệt bài này? OK để đăng hoặc sửa: ..."
4. Nếu OK: mở browser và đăng bài
5. Báo link sau khi đăng, lưu vào memory

## Quy tắc
- Luôn xin duyệt trước khi đăng
- Tiếng Việt có dấu, tone chuyên nghiệp
- Kèm hashtag phù hợp
- Không share thông tin cá nhân
""")
        print("  \u2705 Da tao SOUL.md cho workspace-social")
    else:
        print("  \u2139\ufe0f SOUL.md da ton tai, bo qua")

    # Step 8: Ghi config
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print("")
    print("  ===================================")
    print("  \u2705 Merge hoan tat!")
    print("  ===================================")
    print(f"     Config: {config_path}")
    print(f"     Workspace: {workspace_path}")
    print(f"     OS: {SYSTEM}")
    print("")

    if bot_token:
        print("  \u25b6\ufe0f Tiep theo: openclaw gateway restart || openclaw gateway start")
    else:
        print("  \u26a0\ufe0f NHO sua botToken trong config truoc khi khoi dong!")
        print("     Mo file: " + config_path)
        print("     Tim 'botToken' va nhap token that vao.")
        print("  \u25b6\ufe0f Sau do: openclaw gateway restart || openclaw gateway start")

    print("")


if __name__ == "__main__":
    main()
