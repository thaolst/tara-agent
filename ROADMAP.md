# Roadmap

> Lộ trình phát triển Tara Agent. Mỗi phase khoảng 2-4 tuần, tùy theo phản hồi từ người dùng.

## Phase 1: Social Auto-Pilot (MVP)

Mục tiêu: 1 AI có thể đăng bài lên LinkedIn, Facebook, Threads từ lệnh Telegram.

| Tính năng | Mô tả |
|---|---|
| Soạn bài LinkedIn | Draft + duyệt + đăng tự động |
| Soạn bài Facebook | Draft + duyệt + đăng tự động |
| Soạn bài Threads | Draft + duyệt + đăng tự động |
| Archive GitHub | Lưu bài đã đăng vào memory |
| Config mẫu | File openclaw.json cho người mới |

## Phase 2: Lịch đăng bài

Mục tiêu: Đặt lịch trước, AI tự động nhắc và hỏi bạn trước giờ đăng.

| Tính năng | Mô tả |
|---|---|
| Lịch tuần | Kế hoạch đăng bài cho cả tuần |
| Nhắc nhở | AI nhắc bạn 30p trước giờ đăng |
| Nội dung từ kho | Lấy từ knowledge base có sẵn |
| Lịch định kỳ | Lặp lại hàng tuần |

## Phase 3: Campaign Tracking

Mục tiêu: Theo dõi hiệu quả bài đăng, campaign.

| Tính năng | Mô tả |
|---|---|
| Thống kê tương tác | Lượt thích, comment, share |
| So sánh campaign | Bài nào chạy tốt nhất |
| Báo cáo tuần | AI tổng kết hiệu quả hàng tuần |

## Phase 4: Mở rộng

Mục tiêu: Ghép thêm use case khác ngoài social.

| Tính năng | Mô tả |
|---|---|
| Competitor monitor | Theo dõi bài đăng của đối thủ |
| Price tracker | Giống tara-bot flight search |
| Knowledge base | Lưu học từ mới vào repo |
| Notion backup | Tự động backup lên Notion |

## Nguyên tắc phát triển

- 1 tính năng / phase. Không làm quá nhiều cùng lúc.
- Nhận phản hồi từ người dùng trước khi thêm tính năng mới.
- Code + config luôn đi kèm docs.
- Tiếng Việt có dấu là chính. Tiếng Anh trong details.

---

<details>
<summary>English version</summary>

## Roadmap

Development roadmap for Tara Agent. Each phase takes about 2-4 weeks, depending on user feedback.

### Phase 1: Social Auto-Pilot (MVP)
Goal: One AI that can post to LinkedIn, Facebook, and Threads from Telegram commands.

Features: LinkedIn drafts, Facebook drafts, Threads drafts, GitHub archive, sample config.

### Phase 2: Posting Schedule
Goal: Schedule posts in advance. AI reminds you before posting time.

Features: Weekly calendar, 30-min reminders, content from knowledge base.

### Phase 3: Campaign Tracking
Goal: Track post performance and campaign effectiveness.

Features: Engagement stats (likes, comments, shares), campaign comparison, weekly reports.

### Phase 4: Expansion
Goal: Add more use cases beyond social posting.

Features: Competitor monitoring, price tracking (from tara-bot), knowledge base, Notion backup.

### Development principles
- One feature per phase. No multitasking.
- Collect user feedback before adding new features.
- Always document alongside code and config.
- Vietnamese first with full diacritics. English in details.

</details>
