#!/usr/bin/env python3
"""Ghép cấu hình Tara Agent vào OpenClaw config hiện tại."""

import json
import os
import sys

CONFIG_PATH = os.path.expanduser("~/.openclaw/openclaw.json")
WORKSPACE_PATH = os.path.expanduser("~/.openclaw/workspace-social")

tara_agent_config = {
    "channels": {
        "telegram": {
            "enabled": True,
            "botToken": "123456:ABC-def_ghi",
            "dmPolicy": "open",
            "allowFrom": ["*"],
            "groupPolicy": "disabled"
        }
    },
    "agents": {
        "list": [
            {
                "id": "social",
                "name": "Tara Social Agent",
                "workspace": "/Users/<your-username>/.openclaw/workspace-social",
                "identity": {
                    "emoji": "📢"
                },
                "subagents": {
                    "allowAgents": []
                }
            }
        ]
    },
    "bindings": [
        {
            "match": {
                "channel": "telegram",
                "peer": {
                    "kind": "dm",
                    "id": "*"
                }
            },
            "agentId": "social"
        }
    ]
}


def merge_dict(base, override):
    """Merge override vào base, sâu đến 2 levels."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            base[key].update(value)
        elif key in base and isinstance(base[key], list) and isinstance(value, list):
            base[key].extend(value)
        else:
            base[key] = value
    return base


def main():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Không tìm thấy config tại: {CONFIG_PATH}")
        print("   Chạy 'openclaw onboard' trước để tạo config mặc định.")
        sys.exit(1)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    # Merge channels
    if "channels" not in config:
        config["channels"] = {}
    config["channels"]["telegram"] = tara_agent_config["channels"]["telegram"]

    # Merge agents
    if "agents" not in config:
        config["agents"] = {"list": []}
    # Kiểm tra xem social agent đã tồn tại chưa
    existing_ids = [a.get("id") for a in config["agents"].get("list", [])]
    if "social" not in existing_ids:
        config["agents"]["list"].append(tara_agent_config["agents"]["list"][0])
        print("✅ Đã thêm social agent")
    else:
        print("ℹ️  Social agent đã tồn tại, bỏ qua")

    # Merge bindings
    if "bindings" not in config:
        config["bindings"] = []
    # Kiểm tra binding đã tồn tại chưa
    existing_bindings = [b for b in config["bindings"] if b.get("agentId") == "social"]
    if not existing_bindings:
        config["bindings"].extend(tara_agent_config["bindings"])

    # Tạo workspace nếu chưa có
    os.makedirs(WORKSPACE_PATH, exist_ok=True)
    soul_path = os.path.join(WORKSPACE_PATH, "SOUL.md")
    if not os.path.exists(soul_path):
        with open(soul_path, "w") as f:
            f.write("""# SOUL.md - Tara Social Agent

Ban la Tara Social Agent. Nhiem vu: giup nguoi dung soan va dang bai len LinkedIn, Facebook, Threads.

## Quy trinh
1. Nguoi dung gui lenh tren Telegram: "soan bai linkedin", "soan bai facebook", "soan bai threads"
2. Ban soan draft theo style tung nen tang
3. Gui draft lai, hoi: "Duyet bai nay? OK de dang hoac sua: ..."
4. Neu OK: mo browser va dang bai
5. Bao link sau khi dang, luu vao memory

## Style tung nen tang
- LinkedIn: chuyen sau, insight-driven (800-1200 tu)
- Facebook: gan gui, cam xuc, cau chuyen ca nhan (200-500 tu)
- Threads: ngan gon, conversational, gay to mo (duoi 500 ky tu)

## Quy tac
- Luon xin duyet truoc khi dang
- Tieng Viet co dau, tone chuyen nghiep
- Kem hashtag phu hop
- Khong share thong tin ca nhan cua nguoi dung
""")
        print("✅ Đã tạo SOUL.md cho workspace-social")

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\n✅ Merge hoàn tất!")
    print(f"   Config: {CONFIG_PATH}")
    print(f"   Workspace: {WORKSPACE_PATH}")
    print("\n⚠️  Nhớ sửa botToken + workspace path trong file config!")
    print("   Tiếp theo: openclaw gateway restart")


if __name__ == "__main__":
    main()
