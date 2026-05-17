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
| Mất/lỡ thiết bị | Config trên GitHub, deploy lại dễ dàng |

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
# 1. Cài OpenClaw
npm install -g openclaw@latest
openclaw onboard

# 2. Clone repo và ghép tự động
git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

# 3. Script sẽ hỏi botToken -> nhập vào (token được ẩn khi gõ)
# 4. Restart gateway
openclaw gateway restart || openclaw gateway start
```

**macOS note:** Python có sẵn. Chỉ cần cài Node.js.

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

### Windows

Windows có **2 cách**. Cách nào cũng được.

#### Cách 1: Git Bash (dễ nhất)

1. Cài **Node.js** từ https://nodejs.org (tick "Add to PATH")
2. Cài **Git for Windows** từ https://git-scm.com (tick "Git Bash" + "Git from the command line")
3. Mở **Git Bash**
4. Chạy:

```bash
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart || openclaw gateway start
```

#### Cách 2: WSL (Windows Subsystem for Linux)

1. Mở PowerShell (Admin), chạy:

```powershell
wsl --install -d Ubuntu
```

2. Restart máy, mở **Ubuntu** từ Start Menu
3. Trong WSL terminal, chạy:

```bash
sudo apt update && sudo apt install nodejs npm python3 git -y
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart || openclaw gateway start
```

**Windows note:** Nếu `python3` không tìm thấy, thử `python merge_config.py`.

## Nếu bị crash (lỗi gateway)

Nguyên nhân thường gặp:

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

</details>
