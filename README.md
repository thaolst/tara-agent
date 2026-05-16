# Tara Agent

> AI ca nhan cua ban tren Telegram. Bat dau bang social auto-pilot, mo rong dan.

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

## Bat dau nhanh

`ash
# 1. Cai OpenClaw
npm install -g openclaw@latest
openclaw onboard

# 2. Tao Telegram bot (qua @BotFather)
# 3. Copy config mau tu repo nay
# 4. Restart va test
`

Xem file trong social/ va config/ de biet chi tiet.

## Cap truc repo

`
tara-agent/
├── README.md          # Gioi thieu
├── ROADMAP.md         # Loi trinh phat trien
├── config/            # File cau hinh OpenClaw mau
├── social/            # Social auto-pilot workflow
├── workflow.md        # Quy trinh chung
└── LICENSE            # MIT
`

## License

MIT -- use freely, share widely.

---

<details>
<summary>English version</summary>

## Tara Agent

Your personal AI agent on Telegram. Start with social auto-pilot, expand as needed.

Tara Agent is a blueprint for a personal AI that takes commands from Telegram, drafts and posts content to LinkedIn, Facebook, and Threads. No API keys needed. No coding required. Just OpenClaw + a Telegram bot.

### Quick start
1. Install OpenClaw
2. Create a Telegram bot via @BotFather
3. Copy the sample config from this repo
4. Restart and test

### Why Tara Agent?

| Problem | Solution |
|---|---|
| Manual posting on multiple platforms | Telegram command, AI does the work |
| Content creation takes too long | AI drafts, you approve quickly |
| Dont know how to code | Just copy a config file |
| Fear of losing data when computer is taken | Daily backup to GitHub |
| Company laptop reclaimed | Config on GitHub, redeploy instantly |

</details>