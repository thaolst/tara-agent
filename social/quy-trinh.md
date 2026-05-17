# Quy trình đăng bài

## 1. Gửi lệnh trên Telegram

Gửi tin nhắn cho bot Telegram của bạn:
- `"soan bai linkedin"` — soạn draft cho LinkedIn
- `"soan bai facebook"` — soạn draft cho Facebook
- `"soan bai threads"` — soạn draft cho Threads
- `"dang bai len linkedin: [nội dung]"` — đăng trực tiếp

## 2. AI soạn draft

AI sẽ soạn nội dung theo style từng nền tảng:
- **LinkedIn:** chuyên sâu, chuyên nghiệp
- **Facebook:** gần gũi, cảm xúc
- **Threads:** ngắn gọn, conversational

## 3. Bạn duyệt

AI gửi draft lại Telegram.
Bạn có thể:
- `"ok"` hoặc `"dang"` -> xác nhận đăng
- `"sua: [nội dung mới]"` -> yêu cầu chỉnh sửa
- `"huy"` -> hủy bỏ

## 4. AI đăng

Khi bạn OK, AI mở browser và đăng bài.
Báo lại: "Đã đăng xong! Link: ..."

## 5. Archive

Bài đăng tự động được lưu vào memory.
Cuối ngày push lên GitHub backup.

---

<details>
<summary>English version</summary>

## Posting Workflow

### 1. Send command on Telegram
- "soan bai linkedin" -> draft for LinkedIn
- "soan bai facebook" -> draft for Facebook
- "soan bai threads" -> draft for Threads

### 2. AI drafts
AI writes content in platform-appropriate style.

### 3. You review
Reply "ok" to approve, "sua: ..." to edit, or "huy" to cancel.

### 4. AI posts
When approved, AI opens browser and publishes.

### 5. Archive
Posts saved to daily memory. Pushed to GitHub at end of day.

</details>
