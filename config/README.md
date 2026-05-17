# Cấu hình mẫu cho Tara Agent (OpenClaw)

Đây là config mẫu để chạy Tara Agent trên máy của bạn.

## Cách dùng

```bash
# 1. Tạo workspace riêng cho social agent
mkdir -p ~/.openclaw/workspace-social

# 2. Copy file config
cp openclaw.json ~/.openclaw/openclaw.json

# 3. Sửa 2 chỗ trong file config:
#    - botToken: thay bằng token từ @BotFather
#    - workspace: thay <username> bằng tên user thật
#      (chạy lệnh 'whoami' để biết)

# 4. Restart Gateway
openclaw gateway restart

# 5. Gửi tin nhắn cho bot:
#    "soan bai linkedin" -> test thử
```

## Cấu trúc config

| Key | Mô tả |
|---|---|
| `channels.telegram.botToken` | Token bot Telegram từ @BotFather |
| `channels.telegram.dmPolicy` | Chính sách DM: `"open"` (ai cũng gửi được) |
| `agents.list[0].workspace` | Path đến workspace của social agent |
| `bindings` | Route Telegram DM đến agent `social` |

## Yêu cầu

- OpenClaw đã cài đặt
- Telegram bot token từ @BotFather
- Đã login LinkedIn, Facebook, Threads trên browser (CrawBot)
- Workspace `~/.openclaw/workspace-social` đã tồn tại

## Lưu ý

- `dmPolicy: "open"` cho phép tất cả DM. Nếu muốn bảo mật, đổi thành `"pairing"` hoặc `"allowlist"` kèm `allowFrom` là Telegram user ID của bạn
- `groupPolicy: "disabled"` — bot không hoạt động trong group
- File config này dùng **JSON** thuần (không dùng JSON5). Không có comment, không có trailing comma
