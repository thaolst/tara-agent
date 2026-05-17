# Cấu hình mẫu cho Tara Agent (OpenClaw)

Đây là config mẫu để chạy Tara Agent trên máy của bạn.

## Cách dùng

1. Copy file này vào OpenClaw config:
```bash
cp openclaw.json ~/.openclaw/openclaw.json
```

2. Sửa `botToken` bằng token từ @BotFather

3. Restart Gateway:
```bash
openclaw gateway restart
```

4. Gửi tin nhắn "soan bai linkedin" cho bot Telegram để test

## Cấu trúc config

- **channel telegram**: kết nối bot Telegram, DM route tới social agent
- **agent social**: agent chuyên soạn và đăng bài social media
- **browser**: dùng CrawBot browser để đăng bài

## Yêu cầu

- OpenClaw đã cài đặt
- Telegram bot token từ @BotFather
- Đã login LinkedIn, Facebook, Threads trên browser (CrawBot)

## Lưu ý

- `dmPolicy: "open"` — cho phép tất cả DM. Nếu muốn bảo mật, đổi thành `"pairing"` hoặc `"allowlist"` với `allowFrom` là Telegram user ID của bạn.
- `groupPolicy: "disabled"` — bot không hoạt động trong group.
