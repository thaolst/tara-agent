# Cấu hình mẫu cho Tara Agent (OpenClaw)

## Cách dùng

File `openclaw.json` này là **phần cấu hình cho Tara Agent**. Bạn cần ghép (merge) nó vào file `~/.openclaw/openclaw.json` hiện tại.

### Cách 1: Thủ công (khuyên dùng)

1. Mở file config hiện tại:
```bash
nano ~/.openclaw/openclaw.json
```

2. Thêm các block sau vào đúng vị trí. Nếu key đã tồn tại, merge nội dung bên trong.

**Block A — Telegram channel** (thêm vào cuối file, trước dấu `}` cuối cùng):
```json
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "<token-tu-BotFather>",
      "dmPolicy": "open",
      "allowFrom": ["*"],
      "groupPolicy": "disabled"
    }
  }
```

**Block B — Social agent** (thêm vào `agents.list`):
```json
    {
      "id": "social",
      "name": "Tara Social Agent",
      "workspace": "/Users/<username>/.openclaw/workspace-social",
      "identity": {
        "emoji": "📢"
      },
      "subagents": {
        "allowAgents": []
      }
    }
```

**Block C — Bindings** (thêm vào root level, cùng cấp với `agents`):
```json
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
```

3. Tạo workspace cho social agent:
```bash
mkdir -p ~/.openclaw/workspace-social
```

4. Copy file SOUL.md từ repo:
```bash
cp workspace-social/SOUL.md ~/.openclaw/workspace-social/
```

5. Restart Gateway:
```bash
openclaw gateway restart
```

### Cách 2: Copy toàn bộ (chỉ dùng cho máy mới cài)

Nếu bạn chưa có config nào, clone repo này và chạy script ghép tự động:
```bash
cd tara-agent
python3 merge_config.py
```

Script này sẽ lấy config mặc định của OpenClaw và ghép Tara Agent vào.

## Cấu trúc

| Key | Mô tả | Bắt buộc sửa |
|---|---|---|
| `channels.telegram.botToken` | Token bot Telegram từ @BotFather | ✅ Có |
| `agents.list[0].workspace` | Path đến workspace của social agent | ✅ Có (thay username) |

## Yêu cầu

- OpenClaw đã cài đặt (`npm install -g openclaw@latest`)
- Telegram bot token từ @BotFather
- Đã login LinkedIn, Facebook, Threads trên browser (CrawBot)

## Lưu ý

- `dmPolicy: "open"` cho phép tất cả DM. Đổi thành `"pairing"` nếu muốn bảo mật
- `groupPolicy: "disabled"` — bot không hoạt động trong group
- File config dùng **JSON thuần** — không có comment, không trailing comma
