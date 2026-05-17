#!/usr/bin/env python3
"""Ghép cấu hình Tara Agent vào OpenClaw config hiện tại.

Hoạt động trên macOS, Linux, và Windows."""

import json
import os
import sys
import platform

CONFIG_PATH = os.path.expanduser("~/.openclaw/openclaw.json")
WORKSPACE_PATH = os.path.expanduser("~/.openclaw/workspace-social")

# Phát hiện OS
SYSTEM = platform.system()  # 'Darwin', 'Linux', 'Windows'


def get_workspace_path():
    """Trả về path workspace phù hợp với OS."""
    raw_path = os.path.expanduser("~/.openclaw/workspace-social")
    # Chuẩn hoá separator theo OS
    return os.path.normpath(raw_path)


def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Không tìm thấy config tại: {CONFIG_PATH}")
        print("   Chạy 'openclaw onboard' trước để tạo config mặc định.")
        sys.exit(1)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    workspace_path = get_workspace_path()

    # Merge channels
    if "channels" not in config:
        config["channels"] = {}
    config["channels"]["telegram"] = {
        "enabled": True,
        "botToken": "123456:ABC-def_ghi",
        "dmPolicy": "open",
        "allowFrom": ["*"],
        "groupPolicy": "disabled"
    }

    # Merge social agent
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
        print(f"✅ Đã thêm social agent (workspace: {workspace_path})")
    else:
        print("ℹ️  Social agent đã tồn tại, bỏ qua")

    # Merge bindings
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
        print("✅ Đã thêm bindings cho Telegram DM → social agent")

    # Tạo workspace nếu chưa có
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
        print("✅ Đa tao SOUL.md cho workspace-social")

    # Ghi config
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\n✅ Merge hoan tat!")
    print(f"   Config: {CONFIG_PATH}")
    print(f"   Workspace: {workspace_path}")
    print(f"   OS: {SYSTEM}")
    print("\n⚠️  Nho sua botToken trong file config!")
    print("   Tiep theo: openclaw gateway restart")


if __name__ == "__main__":
    main()
