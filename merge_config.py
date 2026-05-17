#!/usr/bin/env python3
"""Ghép cau hinh Tara Agent vao OpenClaw config hien tai.

Hoat dong tren macOS, Linux, va Windows.
Tu dong kiem tra prerequisite truoc khi ghi config."""

import json
import os
import sys
import platform
import subprocess
import re

SYSTEM = platform.system()


# ----- PREREQ CHECKS -----

def check_node():
    """Kiem tra Node.js co duoc cai dat khong."""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"  ✅ Node.js: {result.stdout.strip()}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("  ❌ Khong tim thay Node.js. Can cai Node.js (https://nodejs.org).")
    return False


def check_openclaw():
    """Kiem tra OpenClaw co duoc cai dat khong."""
    try:
        result = subprocess.run(["openclaw", "--version"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version = result.stdout.strip() or result.stderr.strip()
            print(f"  ✅ OpenClaw: {version}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("  ❌ Khong tim thay OpenClaw. Chay: npm install -g openclaw@latest")
    return False


def check_python():
    """Kiem tra Python 3 (phong than)."""
    print(f"  ✅ Python 3: {sys.version.split()[0]}")
    return True


def check_config_exists():
    """Kiem tra openclaw.json da duoc tao chua."""
    cfg = os.path.expanduser("~/.openclaw/openclaw.json")
    if os.path.exists(cfg):
        print(f"  ✅ Config ton tai: {cfg}")
        return True
    print(f"  ❌ Chua co config tai: {cfg}")
    print("     Chay 'openclaw onboard' truoc de tao config mac dinh.")
    return False


def prompt_bot_token():
    """Hoi nguoi dung nhap botToken. Uu tien env var $BOT_TOKEN."""
    env_token = os.environ.get("BOT_TOKEN", "").strip()
    if env_token:
        print(f"\n  📦 Doc BOT_TOKEN tu environment variable")
        if validate_token(env_token):
            return env_token
        print("  ⚠️  BOT_TOKEN trong env khong hop le, se hoi lai.")

    print("")
    print("  === TELEGRAM BOT TOKEN ===")
    print("  Tao bot tai @BotFather (Telegram) -> /newbot")
    print("  Sau do nhap token ben duoi.")
    if SYSTEM == "Windows":
        token = input("  Bot token: ").strip()
    else:
        try:
            token = input("  Bot token: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  ⚠️  Khong nhap token. Dung lai.")
            sys.exit(1)

    if not token:
        print("  ⚠️  Token trong. Ghi placeholder, se crash khi chay!")
        print("     Chay lai script va nhap token hop le.")
        return None
    if not validate_token(token):
        print("  ⚠️  Token co ve khong dung dinh dang (can co ':' o giua).")
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
    print("  📋 Kiem moi truong...")
    all_ok = True
    all_ok &= check_python()
    all_ok &= check_node()
    all_ok &= check_openclaw()
    all_ok &= check_config_exists()
    print("")

    if not all_ok:
        print("  ⚠️  Thieu mot so thanh phan. Khac phuc roi chay lai.")
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
        print("  ✅ Da them Telegram channel (voi token thuc)")
    else:
        print("  ⚠️  Da them Telegram channel (token gia - can sua sau)")

    # Step 5: Merge social agent
    if "agents" not in config:
        config["agents"] = {"list": []}
    existing_ids = [a.get("id") for a in config["agents"].get("list", [])]

    if "social" not in existing_ids:
        social_agent = {
            "id": "social",
            "name": "Tara Social Agent",
            "workspace": workspace_path,
            "identity": {"emoji": "📢"},
            "subagents": {"allowAgents": []}
        }
        config["agents"]["list"].append(social_agent)
        print(f"  ✅ Da them social agent (workspace: {workspace_path})")
    else:
        print("  ℹ️  Social agent da ton tai, bo qua")

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
        print("  ✅ Da them bindings cho Telegram DM -> social agent")
    else:
        print("  ℹ️  Bindings da ton tai, bo qua")

    # Step 7: Tao workspace + SOUL.md
    os.makedirs(workspace_path, exist_ok=True)
    soul_path = os.path.join(workspace_path, "SOUL.md")
    if not os.path.exists(soul_path):
        with open(soul_path, "w", encoding="utf-8") as f:
            f.write("""# SOUL.md - Tara Social Agent

Ban la social agent. Nhiem vu: soan va dang bai LinkedIn, Facebook, Threads.

## Quy trinh
1. Nguoi dung gui lenh: "soan bai linkedin", "soan bai facebook", "soan bai threads"
2. Ban soan draft theo style tung nen tang
3. Gui draft lai, hoi: "Duyet bai nay? OK de dang hoac sua: ..."
4. Neu OK: mo browser va dang bai
5. Bao link sau khi dang, luu vao memory

## Quy tac
- Luon xin duyet truoc khi dang
- Tieng Viet co dau, tone chuyen nghiep
- Kem hashtag phu hop
- Khong share thong tin ca nhan
""")
        print("  ✅ Da tao SOUL.md cho workspace-social")
    else:
        print("  ℹ️  SOUL.md da ton tai, bo qua")

    # Step 8: Ghi config
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print("")
    print("  ===================================")
    print("  ✅ Merge hoan tat!")
    print("  ===================================")
    print(f"     Config: {config_path}")
    print(f"     Workspace: {workspace_path}")
    print(f"     OS: {SYSTEM}")
    print("")

    if bot_token:
        print("  ▶️  Tiep theo: openclaw gateway restart")
    else:
        print("  ⚠️  NHO sua botToken trong config truoc khi restart!")
        print("     Mo file: " + config_path)
        print("     Tim 'botToken' va nhap token that vao.")
        print("  ▶️  Sau do: openclaw gateway restart")

    print("")


if __name__ == "__main__":
    main()
