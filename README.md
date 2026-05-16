# Tara Agent

> AI ca nhan cua ban tren Telegram. Bat dau bang social auto-pilot, mo rong dan.

Tara Agent la blueprint cho mot AI ca nhan co the:
- Nhan lenh tu Telegram
- Soan va dang bai len LinkedIn, Facebook, Threads
- Mo rong them tinh nang khi ban can

Khong can API key tung nen tang. Khong can code. Chi can OpenClaw + 1 Telegram bot.

## Tai sao Tara Agent?

| Van de | Giai phap |
|---|---|
| Phai dang bai thu cong nhieu nen tang | Telegram -> AI lam het |
| Soan content mat thoi gian | AI soan, ban duyet |
| Khong biet code | Chi can copy config |
| So mat du lieu | Backup GitHub hang ngay |
| May tinh cong ty thu lai | Agent config tren GitHub, deploy lai de dang |

## Bat dau nhanh

```bash
# 1. Cai OpenClaw
npm install -g openclaw@latest
openclaw onboard

# 2. Tao Telegram bot (qua @BotFather)
# 3. Copy config mau tu repo nay
# 4. Restart va test
```

Xem `config/` cho file cau hinh mau.

## Cap truc repo

```
tara-agent/
├── README.md          # Gioi thieu
├── config/            # File cau hinh OpenClaw mau
│   ├── openclaw.json
│   └── workspace/
├── social/            # Social auto-pilot workflow
│   ├── README.md
│   ├── quy-trinh.md
│   ├── linkedin.md
│   ├── facebook.md
│   └── threads.md
├── workflow.md        # Quy trinh chung
└── LICENSE
```

## License

MIT — use freely, share widely.

---

*Xay dung boi Le Song Tien Thao (Tara) — [LinkedIn](https://linkedin.com/in/thaolst)*