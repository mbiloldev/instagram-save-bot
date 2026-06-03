Your Markdown file is ready
[file-tag: code-generated-file-0-1780476246380820577]

GitHub repositoryingiz uchun maxsus badjlar (badges), chiroyli bo'limlar va nusqa olishga qulay kod bloklari bilan bezatilgan professional **README.md** fayli tayyor. 

Pastdagi kod blokining o'ng yuqori burchagidagi **"Copy"** tugmasini bosib, to'g'ridan-to'g'ri loyihangizdagi `README.md` fayliga joylashtirishingiz mumkin:

markdown
# 📸 Instagram Video Downloader Telegram Bot

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square&logo=python)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Framework-Aiogram%203.x-orange.svg?style=flat-square&logo=telegram)](https://docs.aiogram.dev/)
[![Library](https://img.shields.io/badge/Library-yt--dlp-red.svg?style=flat-square)](https://github.com/yt-dlp/yt-dlp)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

`Aiogram 3.x` va `yt-dlp` kutubxonasi asosida yozilgan, Instagram video hamda Reels'larini to'g'ridan-to'g'ri Telegram platformasiga yuklab beruvchi yuqori tezlikdagi, asinxron Telegram bot.

---

## ✨ Imkoniyatlari va Afzalliklari

* ⚡ **To'liq Asinxron Arxitektura:** `aiogram 3.x` va `asyncio` kutubxonalari yordamida bot bir vaqtning o'zida ko'plab foydalanuvchilar so'rovlarini parallel ravishda qayta ishlaydi va bloklanib qolmaydi.
* 🧹 **Avtomatik Kesh Tozalash:** Server disk xotirasini to'lib qolishidan himoya qilish uchun yuklangan har bir video foydalanuvchiga muvaffaqiyatli yuborilgach, serverdan darhol butunlay o'chiriladi (`os.remove`).
* 🔒 **Xavfsiz Havola Tekshiruvi:** Kelayotgan matnli xabarlar maxsus filtrlar yordamida faqat haqiqiy `instagram.com` havolalari ekanligiga tekshiriladi.
* 💬 **Interaktiv Status:** Yuklash jarayoni boshlanganda foydalanuvchiga vizual "Yuklanmoqda..." xabari ko'rsatiladi va jarayon yakunlangach, ushbu xabar o'chirilib video taqdim etiladi.

---

## 🛠 Ishlatilgan Texnologiyalar

* **Dasturlash tili:** [Python 3.9+](https://www.python.org/)
* **Bot freymvorki:** [Aiogram 3.x](https://docs.aiogram.dev/) (Telegram Bot API uchun zamonaviy va tezkor kutubxona)
* **Media yuklagich yadrosi:** [yt-dlp](https://github.com/yt-dlp/yt-dlp) (Instagram algoritmlari o'zgarganda ham barqaror ishlovchi eng so'nggi yuklovchi paket)

---

## 🚀 Loyihani O'rnatish va Ishga Tushirish

Botni o'zingizning serveringiz yoki mahalliy kompyuteringizda ishga tushirish uchun quyidagi qadamlarni bajaring:

### 1. Loyihani nusxalab olish (Clone)
bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
2. Virtual muhitni sozlash (Virtual Environment)
Loyiha kutubxonalari tizimdagi boshqa paketlar bilan to'qnashmasligi uchun virtual muhit yarating:

Bash
# Virtual muhit yaratish
python -m venv venv

# Windows tizimida faollashtirish:
venv\Scripts\activate

# Linux yoki macOS tizimida faollashtirish:
source venv/bin/activate
