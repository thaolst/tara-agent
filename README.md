# Tara Agent

> Trợ lý AI cá nhân của bạn trên Telegram. Bắt đầu bằng social auto-pilot, mở rộng dần.

Tara Agent là blueprint cho một AI cá nhân có thể nhận lệnh từ Telegram, soạn và đăng bài lên LinkedIn, Facebook, Threads. Mở rộng thêm tính năng khi bạn cần.

Không cần API key từng nền tảng. Không cần code. Chỉ cần OpenClaw + 1 Telegram bot.

## Tại sao Tara Agent?

| Vấn đề | Giải pháp |
|---|---|
| Phải đăng bài thủ công nhiều nền tảng | Telegram gửi lệnh, AI làm hết |
| Soạn content tốn nhiều thời gian | AI soạn, bạn duyệt nhanh |
| Không biết lập trình | Chỉ cần copy config mẫu |
| Sợ mất dữ liệu khi mất máy | Backup lên GitHub mỗi ngày |
| Máy tính công ty bị thu hồi | Config trên GitHub, deploy lại dễ dàng |

## Bắt đầu nhanh (macOS / Linux / Windows)

```bash
# 1. Cài OpenClaw
npm install -g openclaw@latest
openclaw onboard

# 2. Clone repo và ghép tự động
git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

# 3. Sửa botToken trong ~/.openclaw/openclaw.json
# 4. Restart
openclaw gateway restart
```

> **Windows:** dùng Git Bash hoặc WSL. Script tự động dùng path đúng.`merge_config.py` nhận diện OS và dùng path phù hợp.
> **macOS:** chạy trực tiếp.

## Cấu trúc repo

```
tara-agent/
├── README.md          # Giới thiệu
├── ROADMAP.md         # Lộ trình phát triển
├── config/            # File cấu hình OpenClaw mẫu
├── social/            # Social auto-pilot workflow
└── LICENSE            # MIT
```

## License

MIT — use freely, share widely.

---

<details>
<summary>English version</summary>

## Tara Agent

Your personal AI agent on Telegram. Start with social auto-pilot, expand as needed.

Tara Agent is a blueprint for a personal AI that takes commands from Telegram, drafts and posts content to LinkedIn, Facebook, and Threads. No API keys needed. No coding required. Just OpenClaw + a Telegram bot.

### Quick start
1. Install OpenClaw
2. Create a Telegram bot via @BotFather
3. Create workspace: `mkdir -p ~/.openclaw/workspace-social`
4. Copy sample config, edit botToken + workspace path
5. Restart and test

### Why Tara Agent?

| Problem | Solution |
|---|---|
| Manual posting on multiple platforms | Telegram command, AI does the work |
| Content creation takes too long | AI drafts, you approve quickly |
| Don't know how to code | Just copy a config file |
| Fear of losing data when computer is taken | Daily backup to GitHub |
| Company laptop reclaimed | Config on GitHub, redeploy instantly |

</details>
