# Tara Agent

<p align="center">
  <img src="https://img.shields.io/github/v/release/thaolst/tara-agent?label=version&color=4ade80&style=flat-square" alt="version" />
  <img src="https://img.shields.io/github/license/thaolst/tara-agent?color=60a5fa&style=flat-square" alt="license" />
  <img src="https://img.shields.io/github/last-commit/thaolst/tara-agent?color=a78bfa&style=flat-square" alt="last commit" />
  <img src="https://img.shields.io/github/stars/thaolst/tara-agent?style=flat-square&color=facc15&logo=github" alt="stars" />
  <img src="https://img.shields.io/badge/AI%20Agent-blue?style=flat-square" alt="type" />
</p>

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
| Mất/lỗi thiết bị | Config trên GitHub, deploy lại dễ dàng |

## Yêu cầu & Kiểm tra

Trước khi bắt đầu, máy tính cần có:
- **Node.js** (>= 18) -- tải về từ https://nodejs.org
- **Python 3** -- macOS/Linux có sẵn, Windows cần tải từ https://python.org
- **Git** -- https://git-scm.com
- **1 Telegram bot token** -- tạo tại @BotFather (Telegram)

Script `merge_config.py` sẽ tự động kiểm tra các yêu cầu này trước khi ghi config.

## Bắt đầu nhanh

### macOS

```bash
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

# Script sẽ hỏi botToken -> nhập vào (token được ẩn khi gõ)
openclaw gateway restart || openclaw gateway start
```

### Linux (Ubuntu/Debian)

```bash
sudo apt install nodejs npm python3 git
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart || openclaw gateway start
```

### Windows (Git Bash)

```bash
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart || openclaw gateway start
```

**Windows note:** Nếu `python3` không tìm thấy, thử `python merge_config.py`. Hoặc dùng WSL (xem README đầy đủ trên GitHub).

## Nếu bị crash (lỗi gateway)

1. **botToken sai hoặc để placeholder** -- Mở `~/.openclaw/openclaw.json`, kiểm tra mục "botToken"
2. **Thiếu Node.js** -- Cài Node.js, chạy lại `npm install -g openclaw@latest`
3. **Telegram bị chặn mạng** -- Thử dùng Telegram bot ở điện thoại kiểm tra trước

Fix nhanh: chạy lại `python3 merge_config.py`, script sẽ hỏi botToken mới.

## Cấu trúc repo

```
tara-agent/
├── README.md          # Giới thiệu
├── ROADMAP.md         # Lộ trình phát triển
├── merge_config.py    # Script ghép config tự động (cross-platform)
├── config/            # File cấu hình OpenClaw mẫu
│   ├── README.md
│   └── openclaw.json
├── social/            # Social auto-pilot workflow
│   ├── README.md
│   ├── noidung-mau.md
│   └── quy-trinh.md
└── LICENSE            # MIT
```

## 👤 Tác giả

**Lê Song Tiên Thảo (Tara)**

Growth Marketing Manager với kinh nghiệm xây dựng agent AI cho growth và social media automation.

🔗 [LinkedIn](https://linkedin.com/in/thaolst) · [Facebook](https://www.facebook.com/LeSongTienThao) · [GitHub](https://github.com/thaolst)

## License

MIT -- use freely, share widely.

---

<details>
<summary>English version</summary>

## Tara Agent

Your personal AI agent on Telegram. Start with social auto-pilot, expand as needed.

Tara Agent is a blueprint for a personal AI that takes commands from Telegram, drafts and posts content to LinkedIn, Facebook, and Threads. No API keys needed. No coding required. Just OpenClaw + a Telegram bot.

### Requirements
- **Node.js** >= 18 (https://nodejs.org)
- **Python 3**
- **Git**
- **Telegram bot token** (from @BotFather)

### Quick start

**macOS / Linux:**
```bash
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

# Script will prompt for botToken (hidden input)
openclaw gateway restart || openclaw gateway start
```

**Windows (Git Bash or WSL):**
- Install Node.js from https://nodejs.org
- Install Git for Windows from https://git-scm.com
- Open Git Bash, then run the same commands above

### If gateway crashes
1. Check `~/.openclaw/openclaw.json` -- make sure `botToken` is not the placeholder
2. Run `python3 merge_config.py` again -- it now prompts for a real token
3. Verify Node.js + OpenClaw are installed

### Why Tara Agent?

| Problem | Solution |
|---|---|
| Manual posting on multiple platforms | Telegram command, AI does the work |
| Content creation takes too long | AI drafts, you approve quickly |
| Don't know how to code | Just copy a config file |
| Fear of losing data when device is taken | Daily backup to GitHub |
| Lost or replaced device | Config on GitHub, redeploy instantly |

### Author

**Lê Song Tiên Thảo (Tara)**

Growth Marketing Manager. Building AI agents for growth and social media automation.

🔗 [LinkedIn](https://linkedin.com/in/thaolst) · [Facebook](https://www.facebook.com/LeSongTienThao) · [GitHub](https://github.com/thaolst)

</details>
