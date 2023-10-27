from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from download_video_audio import download_video, download_audio
import os

bot = Bot(token="6108981524:AAFeNFOO7ZN4uwvHh2yDi4RYZw23nl0Zoc8")
dp = Dispatcher(bot, storage=MemoryStorage())


class States:
    video = "видео"
    audio = "аудио"


@dp.message_handler(state="*", commands=["start"])
async def start_command(message: types.Message):
    keyboard = [[types.KeyboardButton(text='/video')], [types.KeyboardButton(text='/audio')]]
    video_audio_kb = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await message.reply("Добрый день. Я могу скачать видео или аудио с ютуба", reply_markup=video_audio_kb)


@dp.message_handler(state="*", commands=["video"])
async def user_set_state(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.video)
    await message.reply("Я готов скачивать видео", reply=False)


@dp.message_handler(state="*", commands=["audio"])
async def user_set_state(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(States.audio)
    await message.reply("Я готов скачивать аудио", reply=False)



@dp.message_handler(state=States.video)
async def bot_download_video(message: types.Message):
    video_file = await download_video(message.text)
    with open(video_file, "rb") as file:
        await message.reply_video(file, reply=False)
    os.remove(video_file)


@dp.message_handler(state=States.audio)
async def bot_download_audio(message: types.Message):
    audio_file = await download_audio(message.text)
    with open(audio_file, "rb") as file:
        await message.reply_audio(file, reply=False)
    os.remove(audio_file)


if __name__ == '__main__':
    executor.start_polling(dp)
