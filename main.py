import asyncio
import os
import yt_dlp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

BOT_TOKEN = "YOUR_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Instagram video havolasini yuboring!")

@dp.message(F.text)
async def download_video(message: types.Message):
    url = message.text.strip()
    if "instagram.com" not in url:
        await message.answer("Faqat Instagram havolasi yuboring!")
        return

    msg = await message.answer("Yuklanmoqda...")

    try:
        ydl_opts = {
            'outtmpl': f'downloads/%(id)s.%(ext)s',
            'format': 'best',
            'quiet': True,
        }

        os.makedirs('downloads', exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await msg.delete()
        video = types.FSInputFile(filename)
        await message.answer_video(video)
        os.remove(filename)

    except Exception as e:
        await msg.edit_text(f"Xatolik: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
