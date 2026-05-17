# Social Auto-Pilot

Tự động đăng bài lên LinkedIn, Facebook, Threads từ lệnh Telegram.

## Cách hoạt động

```
Telegram (bạn) → AI soạn draft → Bạn duyệt → OK → AI đăng tự động
```

## Yêu cầu

- Tài khoản LinkedIn, Facebook, Threads (đã login trên browser)
- Telegram bot (tạo qua @BotFather)
- OpenClaw (đã cài đặt theo hướng dẫn trong config/)

## Các bước

1. Cài đặt OpenClaw (xem [`config/`](../config))
2. Kết nối Telegram bot (`botToken`)
3. Login các nền tảng social trên browser (CrawBot)
4. Gửi lệnh "soan bai" trên Telegram
5. Duyệt nội dung
6. OK để đăng

## Lưu ý

- Luôn duyệt trước khi đăng
- Tiếng Việt có dấu, tone chuyên nghiệp
- Bài đăng được archive vào memory mỗi ngày
- Backup lên GitHub cuối ngày

---

<details>
<summary>English version</summary>

## Social Auto-Pilot

Auto-post to LinkedIn, Facebook, and Threads from Telegram commands.

### How it works

Telegram (you) -> AI drafts -> You review -> OK -> AI auto-posts

### Requirements
- LinkedIn, Facebook, Threads accounts (logged in on browser)
- Telegram bot from @BotFather
- OpenClaw installed

### Notes
- Always review before posting
- Vietnamese with diacritics, professional tone
- Posts archived to daily memory
- GitHub backup at end of day

</details>
