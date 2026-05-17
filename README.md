# Tara Agent

> Tro ly AI ca nhan cua ban tren Telegram. Bat dau bang social auto-pilot, mo rong dan.

Tara Agent la blueprint cho mot AI ca nhan co the nhan lenh tu Telegram, soan va dang bai len LinkedIn, Facebook, Threads. Mo rong them tinh nang khi ban can.

Khong can API key tung nen tang. Khong can code. Chi can OpenClaw + 1 Telegram bot.

## Tai sao Tara Agent?

| Van de | Giai phap |
|---|---|
| Phai dang bai thu cong nhieu nen tang | Telegram gui lenh, AI lam het |
| Soan content ton nhieu thoi gian | AI soan, ban duyet nhanh |
| Khong biet lap trinh | Chi can copy config mau |
| So mat du lieu khi mat may | Backup len GitHub moi ngay |
| May tinh cong ty bi thu hoi | Config tren GitHub, deploy lai de dang |

---

## Yeu cau & Kiem tra

Truoc khi bat dau, may tinh can co:
- **Node.js** (>= 18) - tai ve tu https://nodejs.org
- **Python 3** - macOS/Linux co san, Windows can tai tu https://python.org
- **Git** - https://git-scm.com
- **1 Telegram bot token** - tao tai @BotFather (Telegram)

Script `merge_config.py` se tu dong kiem tra cac yeu cau nay.

---

## Bat dau nhanh

### macOS

```bash
# 1. Cai OpenClaw
npm install -g openclaw@latest
openclaw onboard

# 2. Clone repo va ghep tu dong
git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

# 3. Script se hoi botToken -> nhap vao
# 4. Restart
openclaw gateway restart
```

**macOS note:** Khong can cai them gi. Python co san. Chi can Node.js.

### Linux (Ubuntu/Debian)

```bash
sudo apt install nodejs npm python3 git
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart
```

### Windows

Windows co **2 cach**. Cach nao cung duoc:

#### Cach 1: Git Bash (de nhat)

1. Cai **Node.js** tu https://nodejs.org (tick "Add to PATH")
2. Cai **Git for Windows** tu https://git-scm.com (tick "Git Bash" + "Git from the command line")
3. Mo **Git Bash**
4. Chay:
```bash
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart
```

#### Cach 2: WSL (Windows Subsystem for Linux)

1. Mo PowerShell (Admin), chay:
```powershell
wsl --install -d Ubuntu
```
2. Restart may, mo **Ubuntu** tu Start Menu
3. Trong WSL terminal, chay:
```bash
sudo apt update && sudo apt install nodejs npm python3 git -y
npm install -g openclaw@latest
openclaw onboard

git clone https://github.com/thaolst/tara-agent.git
cd tara-agent
python3 merge_config.py

openclaw gateway restart
```

**Windows note:** Neu `python3` khong tim thay, thu `python merge_config.py`.

---

## Neu bi crash (loi gateway)

Nguyen nhan thuong gap:
1. **botToken sai hoac de placeholder** -> Mo `~/.openclaw/openclaw.json`, kiem tra muc "botToken"
2. **Thieu Node.js** -> Cai Node.js, chay lai `npm install -g openclaw@latest`
3. **Telegram bi chan mang** -> Thu dung Telegram bot o dien thoai kiem tra truoc

Fix nhanh: chay lai `python3 merge_config.py`, script se hoi botToken moi.

---

## Cau truc repo

```
tara-agent/
├── README.md          # Gioi thieu
├── ROADMAP.md         # Lo trinh phat trien
├── merge_config.py    # Script ghep config tu dong (cross-platform)
├── config/            # File cau hinh OpenClaw mau
│   ├── README.md
│   └── openclaw.json
├── social/            # Social auto-pilot workflow
│   ├── README.md
│   ├── noidung-mau.md
│   └── quy-trinh.md
└── LICENSE            # MIT
```

## License

MIT - use freely, share widely.

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

# Script will prompt for botToken
openclaw gateway restart
```

**Windows (Git Bash or WSL):**
- Install Node.js from https://nodejs.org
- Install Git for Windows from https://git-scm.com
- Open Git Bash, then run the same commands above

### If gateway crashes
1. Check `~/.openclaw/openclaw.json` - make sure `botToken` is not the placeholder
2. Run `python3 merge_config.py` again - it now prompts for a real token
3. Verify Node.js + OpenClaw are installed

### Why Tara Agent?

| Problem | Solution |
|---|---|
| Manual posting on multiple platforms | Telegram command, AI does the work |
| Content creation takes too long | AI drafts, you approve quickly |
| Don't know how to code | Just copy a config file |
| Fear of losing data when computer is taken | Daily backup to GitHub |
| Company laptop reclaimed | Config on GitHub, redeploy instantly |

</details>
